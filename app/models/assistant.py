from app.extensions import db

class Assistant(db.Model):
    __tablename__ = 'assistants'

    assistantId = db.Column(db.String(36), primary_key=True)
    domaine = db.Column(db.String(100), nullable=False)
    expertiseLevel = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    def __init__(self, assistantId, domaine, expertiseLevel, isActive=True):
        self.assistantId = assistantId
        self.domaine = domaine
        self.expertiseLevel = expertiseLevel
        self.isActive = isActive
