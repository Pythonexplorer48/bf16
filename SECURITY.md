# Security Policy
## Supported Versions
The following versions of `bf16` are currently being supported with security updates:
| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0.0 | :x:                |

## Our Commitment to Safety
Because `bf16` utilizes a compiled Windows DLL and x64 Assembly, we prioritize transparency to ensure user trust:
1.  **Open Source Assembly:** The full source code for the DLL (`bf16.asm`) is available in the repository for audit.
2.  **Reproducible Builds:** The `comp.bat` file shows the exact steps used to compile the binary using NASM and GoLink.
3.  **No Hidden Dependencies:** The Python wrapper (`__init__.py`) uses only the standard `ctypes` library.

## Reporting a Vulnerability
If you discover a security vulnerability (such as a buffer overflow in the assembly logic or a binary flaw), please do not report it through public comments or social media.
Instead, please report vulnerabilities by:
*   Opening a private issue on GitHub (if available).
*   Contacting the maintainer directly via GitHub profile details.
I aim to acknowledge all security reports and provide a fix or mitigation as quickly as possible.

## Verification
To ensure you are using an authentic version of this package:
*   Always install via `pip install bf16`.
*   Verify that the version you are using is **Verified** on PyPI via Trusted Publishing (GitHub Actions OIDC).

## Binary Integrity
To ensure the `bf16.dll` you receive is the one I built:
- **Trusted Build:** The DLL is packaged by GitHub Actions directly from this source code.
- **Transparency:** The `bf16.asm` is provided so you can compile it yourself using the included `comp.bat` to verify the bytes match.