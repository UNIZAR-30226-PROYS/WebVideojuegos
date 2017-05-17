#instalamos si no lo esta git
dpkg -l | grep -qw git || apt-get install git

#clonamos el repositiorio
git clone https://github.com/UNIZAR-30226-2017-05/WebVideojuegos.git

#instalamos FLASK
chmod +x WebVideojuegos/web/install.sh
./WebVideojuegos/web/install.sh

#instalamos si no lo esta mysql
dpkg -l | grep -qw mysql-server || apt-get install mysql-server
dpkg -l | grep -qw python-mysqldb || apt-get install python-mysqldb
service mysql start

#creamos y poblamos la base de datos
mysql -u root -p 
source ./WebVideojuegos/web/archivosBBDD/crearBBDD.sql
source ./WebVideojuegos/web/archivosBBDD/crear.sql
exit