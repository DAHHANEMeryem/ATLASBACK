from app.extensions import db
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(36), primary_key=True)  # Changé ici
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def __init__(self, user_id, name, email, password):  # Changé ici aussi
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password