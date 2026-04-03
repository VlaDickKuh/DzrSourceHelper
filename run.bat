@echo off
chcp 65001 >nul
setlocal

set VENV_DIR=.venv
set SCRIPT=main.py

if not exist %VENV_DIR% (
    echo Виртуальное окружение не найдено. Сначала выполните скрипт установки.
    pause
    exit /b 1
)

call %VENV_DIR%\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Не удалось активировать виртуальное окружение.
    pause
    exit /b 1
)

if not exist %SCRIPT% (
    echo Файл %SCRIPT% не найден.
    pause
    exit /b 1
)

python %SCRIPT% %*