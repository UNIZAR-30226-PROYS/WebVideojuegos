#Si no funciona pip actualizamos python
su
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
tar -xvf Python-3.6.0.tgz
cd Python-3.6.0
./configure
make -j8
make altinstall
python3.6
