@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set VENV_DIR=.venv
set REQUIREMENTS=requirements.txt

:: Проверка наличия Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python не найден. Установите Python и добавьте его в PATH.
    pause
    exit /b 1
)

if not exist %VENV_DIR% (
    echo Создание виртуального окружения в папке %VENV_DIR%...
    python -m venv %VENV_DIR%
    if !errorlevel! neq 0 (
        echo Ошибка при создании виртуального окружения.
        pause
        exit /b 1
    )
) else (
    echo Виртуальное окружение уже существует.
)

echo Активация виртуального окружения...
call %VENV_DIR%\Scripts\activate.bat
if !errorlevel! neq 0 (
    echo Не удалось активировать виртуальное окружение.
    pause
    exit /b 1
)

:: Установка зависимостей, если есть requirements.txt
if exist %REQUIREMENTS% (
    echo Установка зависимостей из %REQUIREMENTS%...
    pip install -r %REQUIREMENTS%
    if !errorlevel! neq 0 (
        echo Ошибка при установке зависимостей.
        pause
        exit /b 1
    )
) else (
    echo Файл %REQUIREMENTS% не найден. Установка зависимостей пропущена.
)

call deactivate 

echo Готово.
pause
exit 