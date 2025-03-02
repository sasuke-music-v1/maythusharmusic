from os import path
from typing import Union

from yt_dlp import YoutubeDL

from maythusharmusic.utils.formatters import seconds_to_min
from maythusharmusic.utils.decorators import asyncify


class SoundCloud:
    def __init__(self):
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
        }

    async def valid(self, link: str) -> bool:
        return "soundcloud" in link

    @asyncify
    def download(self, url: str) -> Union[dict, bool]:
        with YoutubeDL(self.opts):
            try:
                info = d.extract_info(url)
            except Exception:
                return False
            xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
            duration_min = seconds_to_min(info["duration"])
            track_details = {
                "title": info["title"],
                "duration_sec": info["duration"],
                "duration_min": duration_min,
                "uploader": info["uploader"],
                "filepath": xyz,
            }
            return track_details, xyz
