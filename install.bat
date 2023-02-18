@echo off

set PYTHON_VERSION=3.9.10

:: Check if OS is Windows
if "%OS%"=="Windows_NT" (

  :: Check if 64-bit Windows
  if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    :: Download 64-bit Python installer
    curl -L -o python.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
    :: Install Python
    python.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
  ) else (
    :: Download 32-bit Python installer
    curl -L -o python.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-embed-win32.zip
    :: Extract Python
    powershell -Command "Expand-Archive python.exe -DestinationPath C:\Python\"
    :: Add Python to PATH
    setx PATH "%PATH%;C:\Python\"
  )
)

:: Check if OS is macOS
if [ "$(uname)" == "Darwin" ]; then
  # Download Python installer
  curl -L -o python.pkg https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-macosx10.9.pkg
  # Install Python
  installer -pkg python.pkg -target /
fi

:: Check if OS is Linux
if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  # Download Python source code
  curl -L -o python.tgz https://www.python.org/ftp/python/%PYTHON_VERSION%/Python-%PYTHON_VERSION%.tgz
  # Extract Python source code
  tar -zxvf python.tgz
  cd Python-%PYTHON_VERSION%
  # Configure Python build
  ./configure --enable-optimizations
  # Build and install Python
  make altinstall
fi

:: Установка Python на Windows
IF "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    msiexec /i python.exe /qb
) ELSE (
    msiexec /i python.exe /qb
)

:: Установка Python на Linux
IF [ "$(uname -s)" == "Linux" ]; then
    apt-get update
    apt-get install -y python3
fi