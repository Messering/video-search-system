using VideSearchSystem.Domain.Entities;
using VideSearchSystem.Domain.Models;

namespace VideSearchSystem.Infrastructure.Data.Models
{
    public class VideoDbSet: Video
    {
        public VideoDbSet()
        {
            Id = Guid.NewGuid();
        }

        public void Load(IList<Scene> credits)
        {
            Scenes = new ScenesCollection();
            Scenes.Add(credits);
        }
    }
}
