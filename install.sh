
#clonamos el repositiorio
git clone https://github.com/UNIZAR-30226-2017-05/WebVideojuegos.git

#instalamos FLASK
chmod +x WebVideojuegos/web/intall.sh
./WebVideojuegos/web/intall.sh

#instalamos si no lo esta mysql
dpkg -l | grep -qw mysql-server || apt-get install mysql-server
dpkg -l | grep -qw MySQL-python || apt-get install MySQL-python
service mysql start

#creamos y poblamos la base de datos
echo "Si solicita contraseña pulsar enter sin escribir nada"
mysql -u root -p -e "source ./WebVideojuegos/web/archivosBBDD/crearBBDD.sql"
mysql -u software -p'software' 'proySoftware' -e "source ./WebVideojuegos/web/archivosBBDD/crearBBDD.sql"

#En construccion