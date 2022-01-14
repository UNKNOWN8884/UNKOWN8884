if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/UNKNOWN8884/UNKOWN8884.git /UNKOWN8884
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /UNKOWN8884
fi
cd /UNKOWN8884
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
