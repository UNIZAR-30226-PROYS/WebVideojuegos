#instalamos git
dpkg -L git >/dev/null 2&>1 || sudo apt-get install -y git

#clonamos el repositiorio
git clone https://github.com/UNIZAR-30226-2017-05/WebVideojuegos.git

#instalamos y/o actualizamos pip
dpkg -L python-pip>/dev/null 2&>1 || sudo apt-get install -y python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

#instalamos FLASK
chmod 0777 WebVideojuegos/web/install.sh
sudo ./WebVideojuegos/web/install.sh

#instalamos si no lo esta mysql
dpkg -L mysql-server || sudo apt-get install mysql-server
dpkg -L python-mysqldb || sudo apt-get install python-mysqldb

sudo service mysql start

#creamos y poblamos la base de datos
echo "Cuando pida la contraseña, introducir la contraseña de mysql de root"
cd ./WebVideojuegos/web/archivosBBDD/
mysql -u root -p < crearBBDD.sql
mysql -u root -p < crear.sql

