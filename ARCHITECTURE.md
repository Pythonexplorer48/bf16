# bf16 Architecture
This document explains the technical design and bit-level logic I used to build the **bf16** project.

## The Design Philosophy
Most libraries use massive C++ runtimes to handle floating-point conversion. I reject that bloat. I interface directly with the CPU using x86-64 Assembly to ensure the smallest possible binary footprint and the lowest latency.

## The Data Path
1.  **Python Layer:** I wrote a thin wrapper to provide a user-friendly interface.
2.  **Ctypes Bridge:** Python uses the `ctypes` library to pass pointers to memory directly to the DLL.
3.  **Assembly Core (The DLL):** I wrote raw x64 machine code to perform the truncation and conversion.
4.  **Return:** The result is passed back to Python as a 2-byte object or a 32-bit float.

## BFloat16 Logic
BFloat16 (Brain Floating Point) is a 16-bit format that maintains the dynamic range of a 32-bit float by truncating the mantissa.

**The Bit-Shift Strategy:**
- A Float32 has 32 bits: `[1 Sign | 8 Exponent | 23 Mantissa]`.
- To convert to BFloat16, I take the 16 most significant bits.
- My logic: `(Float32 >> 16)`
- This leaves: `[1 Sign | 8 Exponent | 7 Mantissa]`.

By doing this in Assembly, I avoid floating-point unit (FPU) overhead and treat the conversion as a simple integer register shift—the fastest operation a CPU can perform.

## Windows x64 ABI Implementation
I designed the DLL to follow the standard Windows x64 Calling Convention:
*   **Registers:** I use RCX, RDX, R8, and R9 for the first 4 arguments.
*   **Shadow Space:** I allocate 32 bytes of "scratch space" on the stack before any API calls (like `ExitProcess`).
*   **Stack Alignment:** I keep the stack 16-byte aligned to prevent crashes during Windows system calls.

## Why I chose Assembly
C++ compilers often add "safety" code and stack guards that increase latency. By writing the core logic myself in NASM/YASM, I ensure that every clock cycle is spent on data conversion, not "bleh" overhead.