@echo off
:: Check Administator Rights
net session >nul 2>&1
if %errorLevel% == 0 (
    goto Main
) else (
    echo Request Administrator Rights
    goto UACPrompt
)
exit /B

:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "%*", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
del "%temp%\getadmin.vbs"
exit /B

:Main
echo Use Admin Mode

:: maybe no necessary
:: call conda activate your_env_name 

pushd "%~dp0"

python .\autoclick.py

pause
