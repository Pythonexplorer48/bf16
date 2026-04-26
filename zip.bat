@echo off
set VERSION=1.0.5
echo Packaging bf16 v%VERSION%...
if exist bf16_v%VERSION%.zip del bf16_v%VERSION%.zip
tar -a -c -f bf16.zip LICENSE README.md bf16
echo Done! Created bf16_v%VERSION%.zip