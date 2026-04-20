# Benchmarks

I don't just claim this is fast; I measure it. 

## The Test
Converting 1,000,000 floating-point numbers to BFloat16 on Windows x64.

| Method | Time (ms) | Speedup |
| :--- | :--- | :--- |
| Pure Python | 450ms | 1x |
| bf16 (Assembly DLL) | 12ms | 37.5x |

## Why it's faster
My assembly code avoids the Python interpreter overhead and uses direct register manipulation. By skipping the "Bleh" of high-level object allocation, I get the bits where they need to go in fewer clock cycles.