using MediatR;
using Microsoft.AspNetCore.Mvc;
using VideSearchSystem.Application.OriginalVideo.Commands;

namespace VideSearchSystem.Api.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class VideoController : ControllerBase
    {
        private readonly IMediator _mediator;

        public VideoController(IMediator mediator)
        {
            _mediator = mediator;
        }

        [HttpPost("upload")]
        public async Task<IActionResult> Upload()
        {
            var videoFile = HttpContext.Request.Form.Files.FirstOrDefault();

            if (videoFile == null || videoFile.Length == 0)
                return BadRequest("Invalid video file.");

            var command = new UploadOriginalVideoCommand(videoFile.FileName, videoFile);
            var result = await _mediator.Send(command);

            return Ok(new { FileName = result });
        }
    }
}
