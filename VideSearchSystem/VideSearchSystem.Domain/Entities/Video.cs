using VideSearchSystem.Domain.Enums;
using VideSearchSystem.Domain.Models;

namespace VideSearchSystem.Domain.Entities
{
    public class Video: IEntity
    {
        public Guid Id { get; protected set; }
        public string Title { get; set; }
        public string Path { get; set; }

        public DateTime UploadDate { get; set; }

        public VideoProcessStatus Status { get; set; }
        public ScenesCollection Scenes { get; set; }

        public VideoMetadata Metadata { get; set; }
    }
}
