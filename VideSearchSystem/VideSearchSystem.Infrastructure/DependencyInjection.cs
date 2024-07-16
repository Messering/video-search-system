using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using VideSearchSystem.Application.Repositories;
using VideSearchSystem.Application.Services;
using VideSearchSystem.Infrastructure.Data;
using VideSearchSystem.Infrastructure.Data.Configurations;
using VideSearchSystem.Infrastructure.Repositories;
using IApplicationDbContext = VideSearchSystem.Infrastructure.Interfaces.IApplicationDbContext;

namespace VideSearchSystem.Infrastructure
{
    public static class DependencyInjection
    {
        public static IServiceCollection AddInfrastructureServices(this IServiceCollection services, IConfiguration configuration)
        {
            services.Configure<ApplicationDatabaseSettings>(configuration.GetSection("MongoDb"));
            services.AddScoped<IApplicationDbContext>(provider => provider.GetRequiredService<ApplicationDbContext>());
            services.AddScoped<IUnitOfWork, UnitOfWork>();

            services.AddScoped<IVideoRepository, VideoRepository>();

            return services;
        }
    }
}
