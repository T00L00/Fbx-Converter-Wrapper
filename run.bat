@echo off
REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Install required packages
pip install -r requirements.txt

REM Run the Python code
python ConvertAllFbx.py

REM Deactivate the virtual environment
call .venv\Scripts\deactivate.bat

echo Done!
pause
