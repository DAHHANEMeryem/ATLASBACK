from app.extensions import db
from app.models.user import User

class Admin(User):
    __tablename__ = 'admins'

    userId = db.Column(db.String(36), db.ForeignKey('users.userId'), primary_key=True)
    isSuperAdmin = db.Column(db.Boolean, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self, userId, name, email, password, isSuperAdmin=False):
        super().__init__(userId=userId, name=name, email=email, password=password)
        self.isSuperAdmin = isSuperAdmin
