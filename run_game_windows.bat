@echo off
setlocal enabledelayedexpansion

REM Check if the main.pyw file exists
if not exist "src\main.pyw" (
    REM If main.pyw does not exist, copy main.py to main.pyw
    copy "src\main.py" "src\main.pyw"
) else (
    REM Get the last modified timestamps of main.py and main.pyw
    for %%I in (src\main.py) do set mainpydate=%%~tI
    for %%I in (src\main.pyw) do set mainpywdate=%%~tI

    REM Compare the timestamps and update main.pyw if main.py is newer
    if "!mainpydate!" GTR "!mainpywdate!" (
        copy /Y "src\main.py" "src\main.pyw"
    )
)

REM Run the game using pythonw without opening a command prompt window
start "" pythonw src\main.pyw

endlocal
