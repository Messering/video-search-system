namespace VideSearchSystem.Application.Services
{
    public interface IUnitOfWork
    {
        Task<int> Save();
    }
}
