#Si no funciona pip actualizamos python
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
sudo chmod 0777 Python-3.6.0.tgz
tar -xvf Python-3.6.0.tgz
sudo chmod 0777 Python-3.6.0
cd Python-3.6.0
./configure --enable-optimizations
make -j8
make altinstall
sudo apt-get update
sudo apt-get upgrade python