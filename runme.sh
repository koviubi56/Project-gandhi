echo Updating pip
pip install -U pip
echo Installing dependencies
pip install -r requirements.txt
echo Checking discord
pip check discord
echo Checking requests
pip check requests
echo -_- RUNNING BOT -_-
python ./main.py
