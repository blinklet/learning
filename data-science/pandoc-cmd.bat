@echo off

REM Add one line for each document in the folder

pandoc -o ".\Pandas-Database-Access.docx" -f markdown -t docx ".\pandas-data-from-database.md" --reference-doc="C:\Users\blinklet\OneDrive - Nokia\DAIS processes\Method of Operations\reference-style-v3.docx"
pandoc -o ".\SQLAlchemy-Pandas.docx" -f markdown -t docx ".\sqlalchemy-minimum.md" --reference-doc="C:\Users\blinklet\OneDrive - Nokia\DAIS processes\Method of Operations\reference-style-v3.docx"

REM Standard error-checking code for every document
IF %ERRORLEVEL% NEQ 0 (
  GOTO errormsg
  ) ELSE (
  GOTO okmsg
  )
:errormsg
echo ERROR! Press Enter key to quit
GOTO done
:okmsg
echo DONE. Press Enter key to quit
:done
pause