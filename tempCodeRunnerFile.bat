
where git >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Git not installed.
    exit /b 1
)

echo ==============================
echo       GitHub Auto Upload
echo ==============================
echo.