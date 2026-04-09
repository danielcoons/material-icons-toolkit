# material-icons-toolkit
A restructured and extended distribution of Material Design Icons with additional pre-generated sizes.


## ✨ Features
- Clean, developer-friendly icon organization
- Pre-generated PNG sizes (24, 30, 40, 48, etc.)
- Script tool to regenerate or extend icon sizes

For an interactive view of all of the images go [here](https://danielcoons.github.io/material-icons-toolkit/examples/gallery.html)

## 📦 Project Structure
```
icons/  
  ├──src/        # Original SVG assets  
  ├── png/        # Generated PNGs by size

scripts/  
  └── processing tools
```

## 🛠️ Development

Install dependencies for scripting:

[Inkscape](https://inkscape.org/release/inkscape-1.4.2/windows/64-bit/msi/dl/)


## 📜 Licensing

This project includes material from the Google Material Design Icons repository:

https://github.com/google/material-design-icons

The project also includes a `batch` file from the following GitHub Gist:

https://gist.github.com/JohannesDeml/779b29128cdd7f216ab5000466404f11 

### Icon Assets

All icon assets (including reorganized and resized versions) are licensed under the Apache License 2.0.  
See the [LICENSE](/LICENSE) file for details.

### Modifications

This repository includes the following modifications:

- Restructured file organization
- Added pre-generated raster icon sizes
- Referenced scripting with `Inkscape` for resizing
- Original Code

All original tooling is licensed under the BSD3 License.
See [LICENSE-BSD3](/LICENSE-BSD3) for details.

## Usage
 - [Download _InkscapeBatchConvert.bat](/scripts/_InkscapeBatchConvert.bat)
 - Put it in the folder where you have files you wish to convert (will also scan on all subfolders for files of input type).
- Then double click the file to start it.

## ⚠️ Disclaimer

This project is not affiliated with or endorsed by Google.
Material Design Icons are property of their respective authors.

## 🙌 Attribution

Material Design Icons by Google:
https://github.com/google/material-design-icons

Licensed under the Apache License 2.0.

GitHub Gist for batch scripting using `Inkscape` found here:
https://gist.github.com/JohannesDeml/779b29128cdd7f216ab5000466404f11
