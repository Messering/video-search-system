namespace VideSearchSystem.Domain.Models
{
    public class KeyframeFeatures
    {
        public List<double> ColorHistogram { get; set; }
        public List<double> TextureFeatures { get; set; }
        public List<double> EdgeFeatures { get; set; }
    }
}
