<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%23f97316&height=170&section=header&text=PDF%20Outline%20Kit&fontSize=40&fontColor=ffffff" alt="PDF Outline Kit banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=22&pause=1000&color=f97316&center=true&vCenter=true&width=650&lines=Turn%20PDF%20bookmarks%20into%20clean%2C%20portable%20outlines" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/pdf-outline-kit"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/pdf-outline-kit"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/pdf-outline-kit"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/pdf-outline-kit"/></p>
<p align="center"><img src="assets/overview.svg" alt="PDF Outline Kit illustration" width="92%"/></p>

## 🧭 Overview
PDF Outline Kit reads a local PDF's bookmark tree and exports it as Markdown or JSON. It is useful for checking document navigation and creating a portable outline without uploading the file.

## ✨ Features
- 📑 Preserves nested bookmark hierarchy.
- 🔢 Includes one-based page numbers when available.
- 🧾 Exports Markdown or JSON for documentation workflows.
- 🔒 Processes files locally and never modifies the source PDF.

## 🎬 Demo
```text
$ python main.py handbook.pdf --format markdown
# Handbook
- Getting started (p. 1)
  - Installation (p. 4)
```
This is a local example, not a hosted demo.

## 🚀 Quick Start
```bash
python -m pip install -r requirements.txt
python main.py handbook.pdf --format markdown
```
Some PDFs contain no outline, and some bookmarks point to destinations without a resolvable page. Those entries are reported with a null page.

## 🧰 Tech Stack
- Python 3.10+
- pypdf for PDF outline reading
- unittest

## 🗂️ Folder Structure
```text
main.py
pdf_outline.py
tests/test_pdf_outline.py
requirements.txt
assets/overview.svg
```

## 🗺️ Roadmap
- [x] Core local workflow
- [x] Documented command-line or browser interface
- [ ] Broader edge-case coverage
- [ ] Optional CI examples

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for bug fixes and document new options.

## 📄 License
Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%23f97316&height=110&section=footer" alt="Animated footer"/></p>
