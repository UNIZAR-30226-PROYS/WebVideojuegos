from proySoftware import bbdd

bbdd.Model.metadata.reflect(bbdd.engine)

class Usuario(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['usuario']
  
class Videojuego(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['videojuego']

class Acciones(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['acciones']
  
class Analisis(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['analisis']

class Desarrolladora(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['desarrolladora']

class DesarrolladoraVideojuego(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['desarrolladora_videojuego']  
  
class Genero(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['genero']  
  
class GeneroVideojuego(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['genero_videojuego']  

class Imagen(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['imagen']

class ImagenVideojuego(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['imagen_videojuego']

class UsuarioVideojuego(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['usuario_videojuego']
  
class Comentario(bbdd.Model):
  __table__ = bbdd.Model.metadata.tables['comentario']
 




