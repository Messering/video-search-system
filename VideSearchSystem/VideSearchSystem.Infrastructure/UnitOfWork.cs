using VideSearchSystem.Application.Services;
using VideSearchSystem.Infrastructure.Interfaces;

namespace VideSearchSystem.Infrastructure
{
    public sealed class UnitOfWork(IApplicationDbContext context) : IUnitOfWork, IDisposable
    {
        public async Task<int> Save()
            => await context.SaveChangesAsync();

        private bool _disposed;

        private void Dispose(bool disposing)
        {
            if (_disposed) return;

            _disposed = true;

            if (disposing)
                context.Dispose();
        }

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }
    }
}
