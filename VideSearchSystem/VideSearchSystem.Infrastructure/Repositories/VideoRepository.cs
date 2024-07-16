using MongoDB.Driver;
using VideSearchSystem.Application.Repositories;
using VideSearchSystem.Infrastructure.Data.Models;
using VideSearchSystem.Infrastructure.Interfaces;

namespace VideSearchSystem.Infrastructure.Repositories
{
    public class VideoRepository: IVideoRepository
    {
        private readonly IApplicationDbContext _context;
        private readonly IMongoCollection<VideoDbSet> _videoDbSet;
    }
}
