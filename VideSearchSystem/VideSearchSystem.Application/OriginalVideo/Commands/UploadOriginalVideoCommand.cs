using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;

namespace VideSearchSystem.Application.OriginalVideo.Commands
{
    public record UploadOriginalVideoCommand : IRequest<string>
    {
        public string Title { get; set; }
        public IFormFile VideoFile { get; set; }

        public UploadOriginalVideoCommand(string title, IFormFile videoFile)
        {
            Title = title;
            VideoFile = videoFile;
        }
    }


    public class UploadOriginalVideoCommandHandler : IRequestHandler<UploadOriginalVideoCommand, string>
    {
        private readonly IWebHostEnvironment _webHostEnvironment;

        public UploadOriginalVideoCommandHandler(IWebHostEnvironment webHostEnvironment)
        {
            _webHostEnvironment = webHostEnvironment;
        }

        public async Task<string> Handle(UploadOriginalVideoCommand request, CancellationToken cancellationToken)
        {
            if (request.VideoFile == null || request.VideoFile.Length == 0)
                throw new ArgumentException("Invalid video file.");

            var uploadsFolderPath = Path.Combine(_webHostEnvironment.WebRootPath, "uploads");
            Directory.CreateDirectory(uploadsFolderPath);

            var fileName = Guid.NewGuid() + Path.GetExtension(request.VideoFile.FileName);
            var filePath = Path.Combine(uploadsFolderPath, fileName);

            using (var fileStream = new FileStream(filePath, FileMode.Create))
            {
                await request.VideoFile.CopyToAsync(fileStream);
            }

            return fileName;
        }
    }
}
