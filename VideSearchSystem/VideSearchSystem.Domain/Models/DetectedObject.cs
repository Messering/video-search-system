namespace VideSearchSystem.Domain.Models
{
    public class DetectedObject
    {
        public string Label { get; set; }
        public double Confidence { get; set; }
        public BoundingBox BoundingBox { get; set; }
    }
}
