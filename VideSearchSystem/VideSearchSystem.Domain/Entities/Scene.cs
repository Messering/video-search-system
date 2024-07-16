using VideSearchSystem.Domain.Models;

namespace VideSearchSystem.Domain.Entities
{
    public class Scene: IEntity
    {
        public Guid Id { get; protected set; }
        public Guid VideoId { get; protected set; }
        public double StartTime { get; set; }
        public double EndTime { get; set; }
        public required List<Keyframe> Keyframes { get; set; }
        public required TemporalFeatures TemporalFeatures { get; set; }
        public required ObjectFeatures ObjectFeatures { get; set; }

        public required StatisticalFeatures StatisticalFeatures { get; set; }
    }
}
