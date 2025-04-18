# app/models/search_history.py
from app.extensions import db

class SearchHistory(db.Model):
    __tablename__ = 'search_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)  # snake_case
    query = db.Column(db.String(255), nullable=False)
    result = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<SearchHistory {self.id}>'