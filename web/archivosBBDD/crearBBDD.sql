-- entrar inicialmente a mysql desde la carpeta con el script con: mysql -u root -p
-- luego ejecutar este script con: source ./crearBBDD.sql
-- salir con: exit;
-- apartir de ahora se puede trabajar en la base sin el root con:
-- mysql -u software -p'software' 'proySoftware'
CREATE DATABASE proySoftware;
GRANT USAGE ON proySoftware.* TO software@localhost IDENTIFIED BY 'software';
GRANT ALL PRIVILEGES ON proySoftware.* TO software@localhost ;
FLUSH PRIVILEGES;
