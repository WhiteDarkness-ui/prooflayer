import magic
import exifread
import io

def extract_metadata(filename: str, content: bytes) -> dict:
    mime = magic.from_buffer(content, mime=True)
    data = {"filename": filename, "mime": mime}

    if mime.startswith("image/"):
        try:
            tags = exifread.process_file(io.BytesIO(content), details=False)
            data["exif"] = {k: str(v) for k, v in tags.items()}
        except Exception:
            data["exif"] = {}

    return data
