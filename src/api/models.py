from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favoritos= db.relationship("Favoritos")

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    favoritos= db.relationship("Favoritos")


    def __repr__(self):
        return f'<Personajes {self.nombre}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero":self.genero,
        }
    
class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    habitantes = db.Column(db.Integer, nullable=False)
    favoritos= db.relationship("Favoritos")


    def __repr__(self):
        return f'<Planetas {self.nombre}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "habitantes":self.habitantes,
        }
    
class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    personajes_id=db.Column(db.Integer,db.ForeignKey("personajes.id"))
    planetas_id=db.Column(db.Integer,db.ForeignKey("planetas.id"))

    def __repr__(self):
        return f'<Favoritos {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personajes_id":self.personajes_id,
            "planetas_id":self.planetas_id,

        }