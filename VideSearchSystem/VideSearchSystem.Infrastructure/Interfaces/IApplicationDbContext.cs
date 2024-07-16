using MongoDB.Driver;
using VideSearchSystem.Domain;

namespace VideSearchSystem.Infrastructure.Interfaces
{
    public interface IApplicationDbContext: IDisposable
    {
        MongoClient MongoClient { get;}
        IClientSessionHandle Session { get; }
        Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
        IMongoCollection<T> GetCollection<T>(string name) where T : IEntity;
        void AddCommand(Func<Task> func);
    }
}
