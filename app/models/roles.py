from sqlalchemy.dialects.mysql import JSON
from app.extensions import db

class Role(db.Model):
    __tablename__ = 'roles'
    
    roleId = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    permissions = db.Column(JSON)  # Correction ici
