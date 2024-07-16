using Microsoft.Extensions.Logging;
using System.Diagnostics;

namespace VideSearchSystem.Application.Common.Behaviours;

public class UnhandledExceptionBehaviour<TRequest, TResponse>(ILogger<TRequest> logger) : IPipelineBehavior<TRequest, TResponse> where TRequest : notnull
{
    private readonly ILogger<TRequest> _logger = logger;

    public async Task<TResponse> Handle(TRequest request, RequestHandlerDelegate<TResponse> next, CancellationToken cancellationToken)
    {
        var requestName = typeof(TRequest).Name;
        using var activity = new Activity(requestName).Start();

        try
        {
            return await next();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Unhandled Exception for Request {RequestName} {@Request}", requestName, request);
            throw;
        }
        finally
        {
            activity.Stop();
            _logger.LogInformation("Request {RequestName} completed in {Duration}ms", requestName, activity.Duration.TotalMilliseconds);
        }
    }
}
