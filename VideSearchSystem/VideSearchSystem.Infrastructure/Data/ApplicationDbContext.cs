using Microsoft.Extensions.Options;
using MongoDB.Bson.Serialization.Conventions;
using MongoDB.Bson.Serialization.Serializers;
using MongoDB.Bson.Serialization;
using MongoDB.Bson;
using MongoDB.Driver;
using VideSearchSystem.Infrastructure.Data.Configurations;
using VideSearchSystem.Infrastructure.Interfaces;
using VideSearchSystem.Domain;

namespace VideSearchSystem.Infrastructure.Data
{
    public class ApplicationDbContext : IApplicationDbContext
    {
        private readonly IMongoDatabase _database;
        private readonly List<Func<Task>> _commands;

        public MongoClient MongoClient { get; private set; }
        public IClientSessionHandle? Session { get; private set; }

        public ApplicationDbContext(IOptions<ApplicationDatabaseSettings> settings)
        {
            MongoClient = new MongoClient(settings.Value.ConnectionString);

            _database = MongoClient.GetDatabase(settings.Value.Database);
            _commands = [];
        }

        public static void RegisterConventions()
        {
            BsonSerializer.RegisterSerializer(new GuidSerializer(GuidRepresentation.CSharpLegacy));

            var pack = new ConventionPack
        {
            new IgnoreExtraElementsConvention(true),
            new IgnoreIfDefaultConvention(true)
        };

            ConventionRegistry.Register("Genocs Solution Conventions", pack, _ => true);
        }

        public async Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
        {
            int count = _commands.Count;

            using (Session = await MongoClient.StartSessionAsync(options: null, cancellationToken: cancellationToken))
            {
                Session.StartTransaction();

                try
                {
                    var commandTasks = _commands.Select(c => c());
                    await Task.WhenAll(commandTasks);

                    await Session.CommitTransactionAsync(cancellationToken);
                }
                catch
                {
                    await Session.AbortTransactionAsync(cancellationToken);
                    throw;
                }
                finally
                {
                    _commands.Clear();
                }
            }

            return count;
        }

        public void AddCommand(Func<Task> func) => _commands.Add(func);

        public IMongoCollection<T> GetCollection<T>(string name) where T : IEntity => _database.GetCollection<T>(name);

        private bool _disposed = false;

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        private void Dispose(bool disposing)
        {
            if (!_disposed)
            {
                if (disposing)
                {
                    if (Session != null && Session.IsInTransaction)
                    {
                        Session.AbortTransaction();
                    }

                    Session?.Dispose();
                }

                _disposed = true;
            }
        }
    }
}
