@ECHO OFF 
TITLE Execute python script on anaconda environment
ECHO Please Wait...
:: Section 1: Activate the environment.
ECHO ============================
ECHO Conda Activate
ECHO ============================
@CALL "C:\ProgramData\Anaconda3\Scripts" mssql
:: Section 2: Execute python script.
ECHO ============================
ECHO Python dbsync3.py
ECHO ============================
python H:\python-mssql-sync\dbsync3.py

ECHO ============================
ECHO End
ECHO ============================
