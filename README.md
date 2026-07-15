<div align="center">

# ⚡ Enterprise QR Code Generator Studio

**A production-styled QR code generation platform built with Python & Streamlit**

<img src="screenshots\screencapture-localhost-8501-2026-07-15-15_47_29.png" alt="Enterprise QR Code Generator Studio — full application screenshot" width="800"/>

[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Segno](https://img.shields.io/badge/QR%20Engine-Segno-2E7D32?style=flat-square)](https://pypi.org/project/segno/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](#license)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()

[Overview](#overview) • [Features](#features) • [Tech Stack](#tech-stack) • [Getting Started](#getting-started) • [Usage](#usage) • [Project Structure](#project-structure) • [Roadmap](#roadmap)

</div>

---

## Overview

**QR Code Generator Studio** is a browser-based tool that converts any URL or block of text into a downloadable, standards-compliant QR code. Instead of a bare-bones script, it's built as a configurable studio — giving users fine-grained control over resolution, quiet-zone spacing, color scheme, and ISO error-correction levels, all through a clean, real-time UI.

The project was built to demonstrate practical skills in **rapid UI prototyping with Streamlit**, **binary image handling in Python**, and **wrapping a third-party encoding library (Segno) behind an intuitive, production-flavored interface**.

> 💡 Enter a URL or text string → tune the output parameters → generate and download a print-ready PNG in seconds.

## Features

- 🔗 **Universal Payload Support** — Encode any website URL or free-form text into a scannable QR matrix.
- 🎚️ **Adjustable Resolution** — Configurable scale factor (1–50) to produce anything from thumbnail previews to print-ready assets.
- 📏 **ISO-Compliant Quiet Zone** — Adjustable border width, with guidance based on ISO QR code standards.
- 🎨 **Custom Color Palette** — Live color pickers for foreground and background, enabling on-brand QR codes.
- 🛡️ **Selectable Error Correction (ECC)** — Choose between Level L (7%), M (15%), Q (25%), and H (30%) recovery, so codes stay scannable even with logo overlays or partial damage.
- 📥 **One-Click PNG Export** — Instantly download the generated QR code as a production-ready image file.
- 🔍 **Structural Telemetry Panel** — An expandable JSON view exposing matrix version, encoding mode, ECC level, and color mapping — useful for debugging and technical transparency.
- ⚠️ **Graceful Failsafe Handling** — Input validation and exception handling prevent silent failures during encoding.

<div align="center">
<img src="screenshots\image.png" alt="Sidebar configuration panel screenshot" width="400"/>
<p><em>Sidebar configuration panel — resolution, quiet zone, color pickers, and ECC level in one place.</em></p>
</div>

<div align="center">
<img src="screenshots\image2.png" alt="Custom colored QR code output screenshot" width="400"/>
<p><em>Custom color palette applied to a generated QR code.</em></p>
</div>

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| UI Framework | [Streamlit](https://streamlit.io/) |
| QR Encoding Engine | [Segno](https://pypi.org/project/segno/) |
| Image Handling | Python `io` (in-memory byte buffers) |
| File System | `pathlib` |

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/naman827/QR_code_generator_studio.git
cd QR_code_generator_studio

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install streamlit segno

# 4. Run the app
streamlit run main.py
```

The app will launch in your browser at `http://localhost:8501`.

## Usage

1. Enter a **URL or text payload** in the main input field.
2. Use the sidebar to fine-tune:
   - **Scale (Resolution)** — controls output pixel density.
   - **Border (Quiet Zone)** — controls whitespace margin around the code.
   - **Foreground / Background colors** — via interactive color pickers.
   - **Error Correction Level** — trades storage capacity for damage resistance.
3. The QR code renders instantly in the **Generated Output Viewport**.
4. Click **Download (.png)** to save the asset locally.

<div align="center">
<img src="screenshots\image3.png" alt="Generated QR code output and download button screenshot" width="500"/>
<p><em>Generated output viewport with matrix version/mode caption and download button.</em></p>
</div>

5. Expand **View Code Structural Telemetry** to inspect the underlying matrix version, encoding mode, and configuration as JSON.

<div align="center">
<img src="screenshots\image2.png" alt="Structural telemetry JSON panel screenshot" width="500"/>
<p><em>Structural telemetry panel — matrix version, ECC level, and color mapping exposed as JSON.</em></p>
</div>

## Project Structure

```
QR_code_generator_studio/
├── assets/
│   ├── logo.png                  # App icon
│   ├── hero.png                  # Full app screenshot
│   ├── sidebar-config.png        # Sidebar configuration screenshot
│   ├── color-customization.png   # Custom color output screenshot
│   ├── output-download.png       # Output viewport + download screenshot
│   └── telemetry-panel.png       # Structural telemetry panel screenshot
├── main.py           # Streamlit application entry point
├── .gitignore
└── README.md
```

## Roadmap

- [ ] Batch generation from CSV/Excel input
- [ ] Logo/image overlay embedding on generated codes
- [ ] SVG export alongside PNG
- [ ] QR code scanning/decoding utility
- [ ] Dockerfile for one-command deployment

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Naman**
GitHub: [@naman827](https://github.com/naman827)

---

<div align="center">
<sub>Built with Python & Streamlit</sub>
</div>