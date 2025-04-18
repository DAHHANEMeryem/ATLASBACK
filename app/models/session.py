from app.extensions import db
from datetime import datetime

class Session(db.Model):
    __tablename__ = 'sessions'

    sessionId = db.Column(db.String(36), primary_key=True)
    startTime = db.Column(db.DateTime, default=datetime.utcnow)
    endTime = db.Column(db.DateTime, nullable=True)
    ipAddress = db.Column(db.String(45), nullable=False)  # Pour l'IPv6, 45 caractères suffisent

    def __init__(self, sessionId, startTime=None, endTime=None, ipAddress=None):
        self.sessionId = sessionId
        self.startTime = startTime or datetime.utcnow()  # Si startTime n'est pas fourni, on utilise la date actuelle
        self.endTime = endTime
        self.ipAddress = ipAddress
