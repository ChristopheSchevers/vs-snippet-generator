@echo off
setlocal

REM Run from this script's parent (project root)
pushd "%~dp0\.."

REM Ensure entrypoint exists
if not exist "src\main.py" (
  echo ERROR: src\main.py not found in project root.
  popd
  exit /b 1
)

REM Build with PyInstaller (ensure PyInstaller is installed in PATH/venv)
pyinstaller --onefile src\main.py
if errorlevel 1 (
  echo ERROR: PyInstaller failed.
  popd
  exit /b 1
)

REM Locate executable (dist\main.exe) and move it to scripts\
if exist "dist\main.exe" (
  move /Y "dist\main.exe" "scripts\"
) else (
  echo ERROR: dist\main.exe not found. Listing dist folders:
  dir /s /b dist
  popd
  exit /b 1
)

REM Cleanup build artifacts
rd /s /q build 2>nul || rem
rd /s /q dist 2>nul || rem
del /q main.spec 2>nul || rem

popd
echo Build completed. The executable is located in scripts\main.exe
pause