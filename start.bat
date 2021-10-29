@echo First-time set up will take awhile
@echo Please be patient
py -m venv venv
CALL venv\Scripts\activate
@echo Installing required libraries... This will take awhile
pip install -r requirements.txt
@echo Generating datasets... This will take a while
@echo Ignore the error messages
py scripts/machinelearning.py plot 1
set FLASK_APP=app.py
@echo Now Online
start "" http://127.0.0.1:5000/
flask run
