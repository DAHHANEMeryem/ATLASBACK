from app.extensions import db

class History(db.Model):
    __tablename__ = 'history'

    historyId = db.Column(db.String(36), primary_key=True)
    query = db.Column(db.String(255), nullable=False)

    def __init__(self, historyId, query):
        self.historyId = historyId
        self.query = query
