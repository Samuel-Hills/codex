from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from scripts.asciicheck import lint_utf8_ascii


class TestLintUtf8Ascii(TestCase):
    def test_accepts_crlf_line_endings(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "crlf.md"
            path.write_bytes(b"first line\r\nsecond line\r\n")

            self.assertFalse(lint_utf8_ascii(path, fix=False))
