@echo off
if exist bf16\bf16_dev.dll del bf16\bf16_dev.dll
if not exist bf16 mkdir bf16
set INCLUDE=%cd%\INCLUDE
echo 🛠️ Building DLL into bf16/ folder...
fasm.exe bf16.asm bf16\bf16.dll
if %errorlevel% neq 0 (
    echo ❌ FASM Error!
    pause
    exit /b
)