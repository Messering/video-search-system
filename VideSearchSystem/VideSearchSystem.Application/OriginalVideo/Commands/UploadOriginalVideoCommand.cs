using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;

namespace VideSearchSystem.Application.OriginalVideo.Commands;

public record UploadOriginalVideoCommand(IFormFile VideoFile) : IRequest<string>;

public class UploadOriginalVideoCommandHandler(IWebHostEnvironment webHostEnvironment) : IRequestHandler<UploadOriginalVideoCommand, string>
{
    private readonly IWebHostEnvironment _webHostEnvironment = webHostEnvironment;

    public async Task<string> Handle(UploadOriginalVideoCommand request, CancellationToken cancellationToken)
    {
        if (request.VideoFile is null or { Length: 0 })
            throw new ArgumentException("Invalid video file.", nameof(request.VideoFile));

        var uploadsFolderPath = Path.Combine(_webHostEnvironment.ContentRootPath, "uploads");

        // Ensure the uploads directory exists
        Directory.CreateDirectory(uploadsFolderPath);

        var fileName = $"{Guid.NewGuid()}{Path.GetExtension(request.VideoFile.FileName)}";
        var filePath = Path.Combine(uploadsFolderPath, fileName);

        await using var fileStream = new FileStream(filePath, FileMode.Create);
        await request.VideoFile.CopyToAsync(fileStream, cancellationToken);

        return fileName;
    }
}
