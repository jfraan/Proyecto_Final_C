from app import db

class Propietario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    dni = db.Column(db.String(16), nullable=False)
    mascotas = db.relationship('Mascota', backref='propietario', lazy=True)

class Mascota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    raza = db.Column(db.String(64), nullable=False)
    propietario_id = db.Column(db.Integer, db.ForeignKey('propietario.id'), nullable=False)

    def __repr__(self):
        return f'<Mascota {self.id}: {self.nombre} ({self.raza}), nacida el {self.fecha_nacimiento}>'