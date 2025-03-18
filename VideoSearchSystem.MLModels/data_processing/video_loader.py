import cv2
import os
from config.config import VIDEO_DIR, FRAME_RATE, FRAME_WIDTH, FRAME_HEIGHT

class VideoLoader:
    def __init__(self, video_dir=VIDEO_DIR):
        self.video_dir = video_dir

    def extract_frames(self, video_filename):
        video_path = os.path.join(self.video_dir, video_filename)
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video {video_path} not found")

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        interval = max(1, int(fps // FRAME_RATE))

        frames = []
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % interval == 0:
                resized_frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
                frames.append(resized_frame)

            frame_count += 1

        cap.release()
        return frames
