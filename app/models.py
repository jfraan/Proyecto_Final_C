from app import db

class Mascota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    raza = db.Column(db.String(50), nullable=False)
    propietario_id = db.Column(db.Integer, db.ForeignKey('propietario.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento.strftime('%Y-%m-%d'),
            'raza': self.raza,
            'propietario_id': self.propietario_id
        }


class Propietario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    mascotas = db.relationship('Mascota', backref='propietario', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'mascotas': [mascota.to_dict() for mascota in self.mascotas]
        }
