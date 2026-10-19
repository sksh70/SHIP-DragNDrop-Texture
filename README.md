
# Smart Texture Drag & Drop for Blender

![Blender](https://img.shields.io/badge/Blender-4.1+-orange.svg)

A simple yet powerful Blender addon that streamlines the material creation process. Just drag and drop a texture onto an object, and the addon will automatically find and connect the entire PBR texture set.

![Qi7F6L575g](https://github.com/user-attachments/assets/a06403b0-c6aa-4ffb-866d-718f7c767d8c)


## Key Features

*   **Drag & Drop Workflow:** Simply drag a texture file from your explorer onto any object in the 3D Viewport.
*   **Supported Formats:** PNG, JPG/JPEG, BMP, TIFF, TGA, and DDS (including `.dds` and `.DDS`) for drag and drop and automatic texture-set discovery. DDS files use Blender's native image loader.
*   **Automatic PBR Set Detection:** Intelligently finds and connects maps for Base Color, Metallic, Roughness, and Normals based on filename suffixes.
*   **Two Modes of Operation:**
    1.  **Smart Apply (Default):** Finds and applies the entire texture set automatically.
    2.  **Manual Apply:** Applies only the single dragged texture to a specific input of your choice.
*   **Interactive Control:** Immediately after dropping a texture, press `F9` to open the "Redo Last" panel and switch between modes or change settings.
*   **Intelligent Socket Guessing:** If you drop a file named `MyTexture_normal.png` in manual mode, the addon will correctly default to the "Normal" socket.

## How It Works

The addon's "Smart Apply" feature works by identifying a **base name** from the file you drop and searching for common PBR suffixes.

**Example:** If you drop `Wood_Planks_Normal.png`, the base name is `Wood_Planks`. The addon will then search the same directory for other files like:
*   `Wood_Planks_Color.png`
*   `Wood_Planks_Roughness.png`
*   `Wood_Planks_Metallic.png`

#### Supported Suffixes:
*   **Color:** `_color`, `_albedo`, `_diffuse`, `_basecolor`, `_col`
*   **Metallic:** `_metallic`, `_metal`, `_metalnessmask`
*   **Roughness:** `_roughness`, `_rough`
*   **Normal:** `_normal`, `_nrm`, `_normalgl`

## Installation

1.  Download the packaged add-on ZIP from [**Releases**](https://github.com/sksh70/SHIP-DragNDrop-Texture/releases), or build it from this checkout with `python build_release.py`. The local package is written to `dist/ship_dragndrop_texture-1.1.1.zip`.
2.  In Blender 4.2, go to `Edit` > `Preferences` > `Add-ons`, open the dropdown menu at the top right, and choose `Install from Disk...`.
3.  Select the packaged ZIP, then enable **SHIP Drag and Drop Texture** (version **1.1.1**).

Install the ZIP, rather than selecting `__init__.py` by itself. That filename is the entry point of a package and is not discovered as a standalone add-on. After replacing an older installation, restart Blender so its registered file handlers are refreshed.

## Preparing a Release

Update the version in both `blender_manifest.toml` and `bl_info` in `__init__.py`. When the manifest change reaches `main`, GitHub Actions builds the installable ZIP and attaches it to a draft release. Review the draft under Releases and click Publish; no manual ZIP upload is needed. Enable Actions in your fork if prompted. You can also run **Prepare release** manually from the Actions tab. Existing releases are left unchanged, so use a new version for each release.

## Usage

1.  Drag any texture file from your file browser directly onto an object in the 3D Viewport.
2.  The material is instantly created or updated.
3.  **Immediately after**, press `F9` (or open the "Redo Last" panel at the bottom-left of the viewport) to change the settings:
    *   **`Smart Apply`** (checked by default): Looks for all related textures in the folder.
    *   Uncheck it for **Manual Mode** to only apply the single texture you dropped.
    *   **`Target Socket`**: If in Manual Mode, choose which input to connect the texture to.
