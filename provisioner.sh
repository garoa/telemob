sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

sudo apt-get install -y \
    postgresql-9.3 \
    postgresql-server-dev-9.3 \
    python-dev \
    python-pip

sudo -H pip install --upgrade pip

cd /vagrant
sudo pip install -Ur requirements.txt

echo "cd /vagrant" >> ~/.bashrc
