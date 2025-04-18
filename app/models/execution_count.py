from app.extensions import db

class ExecutionCount(db.Model):
    __tablename__ = 'execution_count'

    typeId = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer, default=0)

    def __init__(self, typeId, name, description, count=0):
        self.typeId = typeId
        self.name = name
        self.description = description
        self.count = count
