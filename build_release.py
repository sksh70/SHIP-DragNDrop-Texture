"""Build an installable Blender extension ZIP without sample assets."""

from pathlib import Path
import tomllib
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    root = Path(__file__).resolve().parent
    manifest = tomllib.loads((root / "blender_manifest.toml").read_text(encoding="utf-8"))
    output = root / "dist" / f"{manifest['id']}-{manifest['version']}.zip"
    output.parent.mkdir(exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for name in ("__init__.py", "blender_manifest.toml", "README.md", "LICENSE"):
            archive.write(root / name, name)
    print(output)


if __name__ == "__main__":
    main()
