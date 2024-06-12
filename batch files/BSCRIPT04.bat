@echo off
setlocal enabledelayedexpansion

:: Define directories
set source_dir=C:\
set archive_dir=Z:\Archive

:: Create archive directory if it does not exist
if not exist "%archive_dir%" (
    mkdir "%archive_dir%"
)

:: Step 1: Sort text files on Drive C: by date and move older files to archive
echo Sorting and moving older text files to %archive_dir%...
forfiles /P "%source_dir%" /S /M *.txt /D -30 /C "cmd /c move @path \"%archive_dir%\""

:: Step 2: Sort archived files by size
echo Sorting archived files by size...
dir "%archive_dir%\*.txt" /O-S /B > "%archive_dir%\sorted_files.txt"

:: Step 3: Prompt user for permission to delete old, large files
echo The following are the largest text files in the archive:
type "%archive_dir%\sorted_files.txt"
echo.

set /p delete_confirm=Do you want to delete these old, large files? (y/n): 
if /i "%delete_confirm%"=="y" (
    for /f %%f in (%archive_dir%\sorted_files.txt) do (
        del "%%f"
    )
    echo Old, large files deleted.
) else (
    echo Files not deleted.
)

:: Clean up
del "%archive_dir%\sorted_files.txt"

echo Task completed.
pause
