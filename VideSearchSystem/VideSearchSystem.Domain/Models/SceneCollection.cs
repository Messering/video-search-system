using System.Collections.ObjectModel;
using VideSearchSystem.Domain.Entities;

namespace VideSearchSystem.Domain.Models
{
    public sealed class ScenesCollection
    {
        private readonly IList<Scene> _scenes;

        public ScenesCollection()
        {
            _scenes = [];
        }

        public void Add(IEnumerable<Scene> scenes)
        {
            foreach (var scene in scenes)
                _scenes.Add(scene);
        }
    }
}
