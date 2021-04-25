echo =_=START=_=
echo -- UPDATING PIP --
pip install -U pip
echo -- INSTALLING DISCORD --
pip install discord
echo - Checking discord -
pip check discord
echo -- INSTALLING REQUESTS --
pip install requests
echo - Checking requests -
pip check requests
echo ---END OF UPDATING, INSTALLING, CHECKING---
echo -_- RUNNING BOT -_-
python ./main.py