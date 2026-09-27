"""A minimal, stdlib-only PNG writer: flat-color rectangles, nothing else.

dm.py's hard constraints rule out Pillow or any other imaging library, so
this draws uncompressed-looking, blocky shapes only. It never renders text,
so a sketch can never carry a hidden message the way a caption could.
"""
import struct
import zlib
from typing import List, Tuple

Color = Tuple[int, int, int]


class Canvas:
    def __init__(self, width: int, height: int, background: Color = (250, 248, 240)) -> None:
        self.width = width
        self.height = height
        self.pixels = bytearray(bytes(background) * (width * height))

    def _in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def set_pixel(self, x: int, y: int, color: Color) -> None:
        if self._in_bounds(x, y):
            i = (y * self.width + x) * 3
            self.pixels[i:i + 3] = bytes(color)

    def fill_rect(self, x0: int, y0: int, x1: int, y1: int, color: Color) -> None:
        for y in range(max(0, y0), min(self.height, y1)):
            row_start = (y * self.width + max(0, x0)) * 3
            row_end = (y * self.width + min(self.width, x1)) * 3
            self.pixels[row_start:row_end] = bytes(color) * ((row_end - row_start) // 3)

    def outline_rect(self, x0: int, y0: int, x1: int, y1: int, color: Color, thickness: int) -> None:
        self.fill_rect(x0, y0, x1, y0 + thickness, color)
        self.fill_rect(x0, y1 - thickness, x1, y1, color)
        self.fill_rect(x0, y0, x0 + thickness, y1, color)
        self.fill_rect(x1 - thickness, y0, x1, y1, color)

    def to_png_bytes(self) -> bytes:
        def chunk(tag: bytes, data: bytes) -> bytes:
            return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data))

        header = struct.pack(">IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0)
        stride = self.width * 3
        raw = bytearray()
        for y in range(self.height):
            raw.append(0)  # filter type 0 (None) at the start of every scanline
            raw.extend(self.pixels[y * stride:(y + 1) * stride])
        body = zlib.compress(bytes(raw), 9)
        return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", body) + chunk(b"IEND", b"")
