# bf16
BF16 is a Python package for converting floating-point numbers to BFloat16 format using optimized Windows x86-64 assembly.

## Live Data
### Pepy.tech data
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/bf16?period=total&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=BLUE&left_text=Total+Downloads)](https://pepy.tech/projects/bf16)[![PyPI Downloads](https://static.pepy.tech/personalized-badge/bf16?period=monthly&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=BLUE&left_text=Downloads+Last+Month)](https://pepy.tech/projects/bf16)[![PyPI Downloads](https://static.pepy.tech/personalized-badge/bf16?period=weekly&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=BLUE&left_text=Downloads+Last+Week)](https://pepy.tech/projects/bf16)
### Github.com data
![Stars](https://img.shields.io/github/stars/Pythonexplorer48/bf16?style=flat-square&color=gold)
![Forks](https://img.shields.io/github/forks/Pythonexplorer48/bf16?style=flat-square&color=blue)
![Open Issues](https://img.shields.io/github/issues/Pythonexplorer48/bf16?style=flat-square&color=red)
![Open PRs](https://img.shields.io/github/issues-pr/Pythonexplorer48/bf16?style=flat-square&color=green)
![License](https://img.shields.io/github/license/Pythonexplorer48/bf16?style=flat-square&color=orange)
![Repo Size](https://img.shields.io/github/repo-size/Pythonexplorer48/bf16?style=flat-square&label=Repo%20Size&color=brightgreen)
![Top Language](https://img.shields.io/github/languages/top/Pythonexplorer48/bf16?style=flat-square&color=8A2BE2)
![Code Size](https://img.shields.io/github/languages/code-size/Pythonexplorer48/bf16?style=flat-square&color=success)
![Last Commit](https://img.shields.io/github/last-commit/Pythonexplorer48/bf16?style=flat-square&color=brightgreen)
![Commit Activity](https://img.shields.io/github/commit-activity/m/Pythonexplorer48/bf16?style=flat-square&color=blueviolet)
![Contributors](https://img.shields.io/github/contributors/Pythonexplorer48/bf16?style=flat-square&color=gold)
![Followers](https://img.shields.io/github/followers/Pythonexplorer48?style=social)
![Watchers](https://img.shields.io/github/watchers/Pythonexplorer48/bf16?style=flat-square&color=blue)
### Pypi.org data
![PyPI Version](https://img.shields.io/pypi/v/bf16?style=flat-square&color=blue)
![Python Versions](https://img.shields.io/pypi/pyversions/bf16?style=flat-square&color=yellow)
### Socket.dev data
[![Socket](https://socket.dev/api/badge/pypi/package/bf16)](https://socket.dev/pypi/package/bf16)
## Virustotal Scan Results
[VirusTotal](https://www.virustotal.com/gui/file/c6dfcebe3aefb6a3835f245576b145b2caff876bf25b3ce44dc58d97689fde30)
### More Badges
![Platform](https://img.shields.io/badge/platform-windows-0078d7?style=flat-square&logo=windows)
![Dependencies](https://img.shields.io/badge/dependencies-none-success?style=flat-square)
![CPU](https://img.shields.io/badge/arch-x86--64-red?style=flat-square)
![Instruction Set](https://img.shields.io/badge/ISA-x64_Assembly-orange?style=flat-square)
![Security Policy](https://img.shields.io/badge/security-policy-brightgreen?style=flat-square)

## Installation
To install bf16 the 2 easiest options are either run this command:
```bash
pip install bf16
```
or click this button to download a zip containing only necessary files to download and also extract it:
[![Download bf16.zip](https://img.shields.io/badge/Download-bf16.zip-blue?style=for-the-badge&logo=windows)](bf16.zip?raw=true)
## Usage
```python
import bf16

x = bf16.bfloat16(3.14)
print(x)  # Outputs the BFloat16 approximation as a float and for the record it also actually output 3.12 because its a real breainfloat16
print(f"Size: {len(x.data)} bytes")  # Always 2 bytes
```

## Requirements
- Windows AMD x86-64
- Python 3.6+
The package includes a compiled assembly executable for fast conversion.

## Acknowledgments
Jeremy Gordon thank you for making golink

## Changelog
### 1.0.1
bf16 has completely changed with the last update here is the main stuff
* added nearly all operators that function that exist within float32 to bfloat16
* instead of bf16.obj and bf16.exe it is now just a bf16.dll
* optimized to not have to open and exit bf16.dll everytime
* added Changelog
* added acknowlegement to golink I forgot
### 1.0.2
bf16 has gained a way for people to know they are downloading a safe package
* corrected README.md old changelog for 1.0.1
* added repo and its link
### 1.0.3
bf16 now has more verified details
* added more verified details
* made SECURITY.md workflow and CODEOWNERS
### 1.0.4
bf16 now has finished documentation.
* Finished community Standards
* Added downloading Zip file allowing you to only download only necessary files saving memory including README.md, LICENSE, bf16/\_\_init__.py, and bf16/bf16.dll
NOTE: go to [[CHANGELOG.md]] for more specific information on the changelog