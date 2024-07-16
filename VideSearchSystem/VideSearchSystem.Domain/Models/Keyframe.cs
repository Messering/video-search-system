namespace VideSearchSystem.Domain.Models
{
    public class Keyframe
    {
        public double Time { get; set; }
        public string Path { get; set; }
        public KeyframeFeatures Features { get; set; }
    }
}
