instalamos git
dpkg -l | grep -qw git || apt-get install git

#clonamos el repositiorio
git clone https://github.com/UNIZAR-30226-2017-05/WebVideojuegos.git

#instalamos y/o actualizamos pip
dpkg -l | grep -qw python-pip || sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

#instalamos FLASK
sudo chmod 0777 WebVideojuegos/web/install.sh
./WebVideojuegos/web/install.sh

#instalamos si no lo esta mysql
dpkg -l | grep -qw mysql-server || sudo apt-get install mysql-server
dpkg -l | grep -qw python-mysqldb || sudo apt-get install python-mysqldb

service mysql start

#creamos y poblamos la base de datos
echo "Cuando pida la contraseña, introducir la contraseña de mysql de root"
cd ./WebVideojuegos/web/archivosBBDD/
mysql -u root -p < crearBBDD.sql
mysql -u root -p < crear.sql
quit