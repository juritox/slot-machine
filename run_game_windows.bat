@echo off
if not exist "src\main.pyw" (
    copy "src\main.py" "src\main.pyw"
)
start "" pythonw src\main.pyw