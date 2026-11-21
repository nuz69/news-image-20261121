#!/usr/bin/env python3
from pathlib import Path
import os
import shutil

def main():
    base_dir = Path(__file__).resolve().parent
    src_path = base_dir / "entry.png"
    if not src_path.is_file():
        raise FileNotFoundError(f"Source image not found: {src_path}")

    output_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_str)
    output_dir.mkdir(parents=True, exist_ok=True)
    dst_path = output_dir / "entry.png"

    shutil.copyfile(src_path, dst_path)

if __name__ == "__main__":
    main()
