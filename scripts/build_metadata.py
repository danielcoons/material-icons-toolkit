#!/usr/bin/env python3

"""
Build icons metadata index

Scans:
  /icons/png/{size}/{icon}.png

Outputs:
  /icons/metadata/icons.json
"""

import json
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parent.parent
ICONS_DIR = ROOT / "icons" / "png"
OUTPUT_DIR = ROOT / "icons" / "metadata"
OUTPUT_FILE = OUTPUT_DIR / "icons.json"


def build_metadata():
    if not ICONS_DIR.exists():
        print(f"❌ icons/png directory not found: {ICONS_DIR}")
        exit(1)

    icon_map = {}

    sizes = [d.name for d in ICONS_DIR.iterdir() if d.is_dir()]
    print(f"🔍 Scanning sizes: {', '.join(sizes)}")

    for size in sizes:
        size_path = ICONS_DIR / size

        for file in size_path.iterdir():
            if not file.is_file() or file.suffix != ".png":
                continue

            name = file.stem

            if name not in icon_map:
                icon_map[name] = {
                    "name": name,
                    "sizes": [],
                    "tags": name.replace("-", "_").split("_")
                }

            try:
                icon_map[name]["sizes"].append(int(size))
            except ValueError:
                continue

    # Convert to sorted list
    icons = []
    for icon in icon_map.values():
        icon["sizes"] = sorted(icon["sizes"])
        icons.append(icon)

    icons.sort(key=lambda x: x["name"])

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Write JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(icons, f, indent=2)

    print(f"✅ Metadata generated: {OUTPUT_FILE}")
    print(f"📦 Total icons: {len(icons)}")


if __name__ == "__main__":
    build_metadata()
