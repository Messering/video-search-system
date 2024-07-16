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
        public async Task<IActionResult> UploadFile(IFormFile file)
        {
            if (file == null || file.Length == 0)
                return BadRequest("No file uploaded");

            var command = new UploadOriginalVideoCommand(file);
            var result = await _mediator.Send(command);

            return Ok(new { FileName = result });
        }
    }
}
