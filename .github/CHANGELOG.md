# Changelog
## 1.0.1
**In this update bf16 has changed immesively!**
### Switched from using bf16.exe and bf16.obj to using bf16.dll
* Decreases files and memory you have to download
* Allows me to use ctypes instead of subprocess making it much faster
### Added many operator functions and more
* bf16 used to have only 3 functions in the \_\_init__.py which where \_\_slots__, \_\_init__, and \_\_repr__ now it has way more
* includes addition truediv floordiv multiplication str is_integer fromhex hex float subtraction xor and more
### Added Changelog to README.md
* Allows for easy direct understanding of versions
### Added Acknowledgements to README.md
* Credits Jeremy Gordon for his incredible work
## 1.0.2
### Corrected bad Changelog implementation
* The old changelog had slightly incorrect information so I corrected it
### Added repo and its link
* lets you see the source code before downloading it plus more files and a wiki
## 1.0.3
### Added more verified details
* pypi used to have more unverified details I fixed that by using a workflow on github
### Made SECURITY.md and CODEOWNERS files
* SECURITY.md allows for people to know that they are safe using bf16 
* CODEOWNERS helps people know who the owner/owners are of the project and adds a few features to pull requests
## 1.0.4
### Finished Near Permanent documentation
* I finished all the documentation I might ever add to bf16 however still some files will normally be changed and if I feel convinced I'll make a new file or change a old file
### Added zip download
* I added a way that lets you download a zip that you can extract and get bf16 without abstraction tax and unwanted files includes readme and license as a reminder
### Finished Community standards
* if you go to insights now on my then go to community standards you'll notice it has a full green bar
### Added more files
* In the repository you'll notice a lot more files that add a lot of extra things on github that change what it does
* The new files are .github/ISSUE_TEMPLATE/bug_report.md, .github/ISSUE_TEMPLATE/optimization_or_feature.md, .github/pull_request_template.md, .github/CONTRIBUTING.md, STATUS.md, SUPPORT.md, zip.bat, bf16.zip, citation.cff, BENCHMARK.md, ARCHITECTURE.md, CHANGELOG.md, and CODE_OF_CONDUCT.md
