CREATE database IF NOT EXISTS proySoftware;
	use proySoftware;
	
CREATE TABLE IF NOT EXISTS usaurio(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	nick varchar(60) NOT null,
	contrasena varchar(300) NOT null,
	genero varchar(1) NOT null,
	fechaRegistro varchar(10) NOT null,
	nombre varchar(140),
	descripcion varchar(500),
	puntMediaUsur int unsigned,
	avatar varchar(300)
);

CREATE TABLE IF NOT EXISTS videojuego(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	titulo varchar(140) NOT null,
	puntnMedia int unsigned
);

CREATE TABLE IF NOT EXISTS analisis(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	analisis varchar(1000) NOT null,
	id_videojuego int unsigned,
	index (id_videojuego),
	foreign key (id_videojuego) references videojuego (id)
		on delete cascade on update no action,
	id_usuario int unsigned,
	index(id_usuario),
	foreign key (id_usuario) references usuario (id)
		on delete cascade on update no action	
);

CREATE TABLE IF NOT EXISTS plataforma(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	nombre varchar(140) NOT null
);

CREATE TABLE IF NOT EXISTS genero(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	nombre varchar(140) NOT null
);

CREATE TABLE IF NOT EXISTS desarrolladora(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	nombre varchar(140) NOT null
);

CREATE TABLE IF NOT EXISTS imagen(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	nombre varchar(140) NOT null,
	principal boolean
);




CREATE TABLE IF NOT EXISTS imagen_videojuego(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	id_videojuego int unsigned,
	index (id_videojuego),
	foreign key (id_videojuego) references videojuego (id)
		on delete cascade on update no action,
	id_imagen int unsigned,
	index(id_imagen),
	foreign key (id_imagen) references imagen (id)
		on delete cascade on update no action
);

CREATE TABLE IF NOT EXISTS plataforma_videojuego(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	id_videojuego int unsigned,
	index (id_videojuego),
	foreign key (id_videojuego) references videojuego (id)
		on delete cascade on update no action,
	id_plataforma int unsigned,
	index(id_plataforma),
	foreign key (id_plataforma) references plataforma (id)
		on delete cascade on update no action
);

CREATE TABLE IF NOT EXISTS genero_videojuego(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	id_videojuego int unsigned,
	index (id_videojuego),
	foreign key (id_videojuego) references videojuego (id)
		on delete cascade on update no action,
	id_genero int unsigned,
	index(id_genero),
	foreign key (id_genero) references genero (id)
		on delete cascade on update no action
);

CREATE TABLE IF NOT EXISTS desarrolladora_videojuego(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	id_videojuego int unsigned,
	index (id_videojuego),
	foreign key (id_videojuego) references videojuego (id)
		on delete cascade on update no action,
	id_desarrolladora int unsigned,
	index(id_desarrolladora),
	foreign key (id_desarrolladora) references desarrolladora (id)
		on delete cascade on update no action
);

CREATE TABLE IF NOT EXISTS usuario_videojuego(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	deseado boolean,
	jugado boolean,
	puntuacion int unsigned,
	id_videojuego int unsigned,
	index (id_videojuego),
	foreign key (id_videojuego) references videojuego (id)
		on delete cascade on update no action,
	id_usuario int unsigned,
	index(id_usuario),
	foreign key (id_usuario) references usuario (id)
		on delete cascade on update no action	
);
CREATE TABLE IF NOT EXISTS acciones(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	accion varchar(60) NOT null,
	fecha date NOT null,
	id_videojuego int unsigned,
	index (id_videojuego),
	foreign key (id_videojuego) references videojuego (id)
		on delete cascade on update no action,
	id_usuario int unsigned,
	index(id_usuario),
	foreign key (id_usuario) references usuario (id)
		on delete cascade on update no action	
);
CREATE TABLE IF NOT EXISTS comentario(
	id int unsigned AUTO_INCREMENT PRIMARY key,
	comentario varchar(1000) NOT null,
	id_analisis int unsigned,
	index (id_analisis),
	foreign key (id_analisis) references analisis (id) 
		on delete cascade on update no action
);
