1) Registrarse en codeanywhere.com

- Entrar en la página y registrarse (y después confirmar el registro entrando
 al link que viene en el correo electrónico que te envían).
 
- Acceder a la cuenta, aparecerá un cuadro de diálogo en el que podremos
 hacer scroll entre un montón de lenguajes con sistema operativo asociado.
 
- Seleccionar Python 3 con CentOS, ponerle el nombre que se quiera y aceptar.

- Tras la creación, se abrirán dos (creo) pestañas por defecto, trabajaremos
 sobre la que es un terminal (línea de comandos).
 

2) Descargar los archivos de la Web

- Crear una carpeta para meter los repositorios de GitHub
 (mkdir github;cd github).
 
- Clonar el repositorio de la Web
 (git clone https://github.com/UNIZAR-30226-2017-05/WebVideojuegos.git).
 

3) Instalar Flask y MySQL

- Entramos en el proyecto (cd WebVideojuegos/web) e instalamos Flask (./install.sh).

- Para instalar e iniciar MySQL hay que seguir los pasos que se dan en la página:
 https://www.ochobitshacenunbyte.com/2015/02/02/crear-una-base-de-datos-mysql-en-gnu-linux/
   Se pide que ejecutemos los siguientes comandos para CentOS (usando sudo por permisos):
   
      sudo yum install mysql-server
      
      sudo /sbin/service mysqld start
      
      sudo chkconfig mysqld on


4) Crear y poblar la Base de Datos

- Accedemos a la carpeta con los archivos de la BBDD (cd archivosBBDD).

- Entrar a MySQL desde la carpeta (mysql -u root -p) y cuando pida contraseña,
 pulsar Enter sin escribir nada (no hay contraseña para root).

- La línea de comandos cambiará a "mysql>".

- Crear la BBDD (source ./crearBBDD.sql).

- Crear las tablas y poblarlas (source ./crear.sql).

- La base de datos ya está creada y poblada, podemos salir (exit;).

Apunte de Dariel:
-- apartir de ahora se puede trabajar en la base sin el root con:
-- mysql -u software -p'software' 'proySoftware'


5) Arrancar el servidor de la página Web

- Volvemos a la carpeta "web" (cd ..).

- Para poder acceder a la BBDD desde el servidor de Flask, instalamos
 el paquete [(yum install MySQL-python) ó (apt get install MySQL-python)].
 
- Arrancamos el servidor (python run.py).

- Se quedará el proceso abierto, ahora vamos a la barra de la izquierda,
 donde aparece el nombre de la máquina virtual que hemos escogido al principio.
 Hacemos click derecho sobre ella y seleccionamos "info".
 
- Aparece una pestaña con información, y en la parte inferior varios links.
 Copiamos el primero de ellos (el primero que NO es https). Ejemplo:
 http://DeLeon-lionwolf10562773.codeanyapp.com
 
- Abrimos una nueva pestaña en nuestro navegador de internet y
 pegamos esta dirección, añadiendo ":8080" al final, que es el puerto que hay
 en los scripts de configuración. Ejemplo:
 http://DeLeon-lionwolf10562773.codeanyapp.com:8080
 
- Debería aparecer la página web en su estado actual.

------ Si algo no es como se explica aquí, hablar con León.
------ Para cualquier consulta técnica, hablar con Dariel.
