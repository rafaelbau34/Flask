import uuid
from app import db


class Rafael(db.Model):
    __tablename__ = 'rafael'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Rafael {self.nombre} {self.apellidos}>'
    
 