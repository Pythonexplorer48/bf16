# bf16
BF16 is a Python package for converting floating-point numbers to BFloat16 format using optimized Windows x86-64 assembly.

## Installation
```bash
pip install bf16
```
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