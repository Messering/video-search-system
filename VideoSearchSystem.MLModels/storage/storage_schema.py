scene_schema = {
    "video_id": str,
    "scene_id": int,
    "frame_start": int,
    "frame_end": int,
    "scene_type": str,
    "features": {
        "temporal": list,
        "spatial": list,
        "object": list
    },
    "created_at": datetime.datetime
}
