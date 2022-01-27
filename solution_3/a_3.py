import yaml
import requests


class VideoFrame:
    def __init__(self, data: bytes, frame: int):
        self.data = data
        self.meta = dict(
            frame=frame,
            size=None,
            detector=Detector(self.data)
        )

    def __repr__(self):
        return f'{self.meta}'

    def resize(self, x, y):
        """resize image"""
        return


class VideoProcessor:
    def __init__(self, filename: str = None, video: bytes = None):
        self.filename = filename
        self.data = video
        self.meta = None
        self.frames = None

    def download_video(self, url: str) -> bytes:
        self.data = requests.get(url).content
        self.meta = self.extract_meta(self.data)
        return True

    def extract_meta(self, video: bytes) -> dict:
        """extra metadata from video"""
        return dict(
            size=None,
            codec=None,
            fps=None,
            exif=None
        )

    def extract_frames(self, video: bytes) -> [VideoFrame]:
        return [VideoFrame]

    def set_framerate(self, fps: int):
        """reduce to N fps"""
        original_framerate = self.meta['fps']

        # pick every N number of frames
        n = original_framerate / fps
        self.frames = self.frames[::n]
        return True

    def toYaml(self) -> yaml:
        meta = [(self.filename, x.meta) for x in self.frames]
        return yaml.dump(meta)

    def toFile(self, filename: str):
        with open(filename, 'w') as f:
            f.write(f'{self.toYaml()}')
        return True

    def trim(self, start: int, end: int):
        """trim to start and end time (in seconds)"""
        start_frame = self.meta['fps'] * start
        end_frame = self.meta['fps'] * end
        self.frames = self.frames[start_frame:end_frame]
        return True


class Detector:

    def __init__(self, frame: VideoFrame):
        self.frame = frame
        self.meta = dict(
            bounding_box=self.bounding_box(),
            objects=self.objects()
        )

    def bounding_box(self, frame: bytes):
        return {}

    def objects(self, frame: bytes):
        return {}

    def __repr__(self):
        return f'{self.meta}'


def main():
    url = 'http://download.openalpr.com/road.mp4'

    video = VideoProcessor()
    video.download_video(url)
    video.trim(0, 60)
    video.set_framerate(5)

    video.toFile('video.yaml')


if __name__ == "__main__":
    main()
