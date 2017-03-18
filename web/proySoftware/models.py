from proySoftware import db


db.Model.metadata.reflect(db.engine)

class Usuario(db.Model):
  __table__ = db.Model.metadata.tables['usuario']


  
class Videojuego(db.Model):
  __table__ = db.Model.metadata.tables['videojuego']

class Acciones(db.Model):
  __table__ = db.Model.metadata.tables['acciones']
  
class Analisis(db.Model):
  __table__ = db.Model.metadata.tables['analisis']

class Desarrolladora(db.Model):
  __table__ = db.Model.metadata.tables['desarrolladora']

class DesarrolladoraVideojuego(db.Model):
  __table__ = db.Model.metadata.tables['desarrolladora_videojuego']  
  
class Genero(db.Model):
  __table__ = db.Model.metadata.tables['genero']  
  
class GeneroVideojuego(db.Model):
  __table__ = db.Model.metadata.tables['genero_videojuego']  

class Imagen(db.Model):
  __table__ = db.Model.metadata.tables['imagen']

class ImagenVideojuego(db.Model):
  __table__ = db.Model.metadata.tables['imagen_videojuego']

class UsuarioVideojuego(db.Model):
  __table__ = db.Model.metadata.tables['usuario_videojuego']
  
class Comentario(db.Model):
  __table__ = db.Model.metadata.tables['comentario']
 




