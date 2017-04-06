# WebVideojuegos ![lgoWeb](https://github.com/UNIZAR-30226-2017-05/WebVideojuegos/blob/master/web/proySoftware/static/img/logo.jpg?raw=true)

## Sobre el Proyecto

El proyecto permite publicar a los usuarios un registro de los videojuegos que han probado con las opiniones y la calificación que creen que estos videojuegos merecen. De este modo, por una parte, sus conocidos pueden enterarse de los videojuegos que han probado e interpretar las opiniones favorables como recomendaciones; y, por otra, los usuarios en general pueden conocer la opinión y el interés que despierta cierto videojuego en quienes ya lo han probado. Los usuarios pueden, así, descubrir nuevos videojuegos interesantes y, en función de la opinión del resto de gente, tanto anónima como conocida, decidir si jugarlos o no.

#### Requisitos del sistema
Consultar:
[Requisitos](https://github.com/UNIZAR-30226-2017-05/WebVideojuegos/blob/master/otros/extras/Requisitos_WebVideojuegos.md)

## Diagramas
#### Vista-Controlador
 ![Modelo Vista-Controlador](https://github.com/UNIZAR-30226-2017-05/WebVideojuegos/blob/master/otros/img/m-v-controlador.jpg?raw=true)

#### Estructura routes-views
 ![Routes-Views](https://github.com/UNIZAR-30226-2017-05/WebVideojuegos/blob/master/otros/img/route-view.jpg?raw=true)
 
#### Tablas y Campos Base de datos
Consultar: 
[BasedeDatos](https://github.com/UNIZAR-30226-2017-05/WebVideojuegos/blob/master/otros/extras/BasedeDatos.md)

#### Diseño de vistas principales
Consultar:
[Vistas](https://github.com/UNIZAR-30226-2017-05/WebVideojuegos/blob/master/otros/extras/pantallas.md)

## Estado actual
Para consultar el estado del proyecto consultar el:
[Listado de tareas realizadas y pendientes](https://github.com/UNIZAR-30226-2017-05/WebVideojuegos/blob/master/web/TODO.md)

#### Listado actual de routes
1. / equivale a /index :
 * Get:
 * requiere(_views/index)
 * devuelve render_template(index, videojuegos:lista) 
 
2. /login : 
 * Get:
 * requiere(_views/registro_login)
 * devuelve render_template(_views/registro_login, data:user_cookies, loginForm:Formulario, registroFormulario) 
 * Post:
 * devuelve /login or / dependiendo del exito o no del proceso de login  
 
3. /loggout es / pero enmascara la funcionalidad de limpiar las cookies de session y usuario 

4. /registro
 * Post:
 * devuelve: routa de /perfilUsuario

5. /perfilUsuario --> declarado, no implementado

#### Listado actual de views
1. _views/index
2. _views/registro_login
3. _views/perfilUsuario --> declarado, no implementado

#### Listado de modelos(modelos de conexion Base de Datos)
0. Usuario
1. Videojuegos
2. Acciones
3. Analisis
4. Desarrolladora
5. DesarrolladoraVideojuego
6. Genero
7. GeneroVideojuego
8. Imagen
9. ImagenVideojuego
10. UsuarioVideojuego
11. Comentario
