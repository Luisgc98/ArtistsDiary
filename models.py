from app import db
from flask_login import UserMixin, current_user
from datetime import datetime, timedelta

class BaseWho(db.Model):
    __abstract__ = True
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_date = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    ovn = db.Column(db.Integer,default=1)
    
    @staticmethod
    def read(object, all=False):
        if all == False:
            return object.query.filter_by(id=object.id).first()
        else:
            return object.query.all()

class BaseMixin(BaseWho):
    __abstract__ = True
    is_active = db.Column(db.String(length=1) ,default='V')
    @staticmethod
    def create(object):
        try: 
            object.created_by = current_user.id
            db.session.add(object)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
        
    @staticmethod
    def update(object):
        try:
            object.ovn = object.ovn + 1
            object.updated_date = datetime.utcnow
            object.updated_by = current_user.id
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
        
    @staticmethod
    def delete(object):
        try: 
            db.session.delete(object)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
        
    @staticmethod
    def deactivate(object):
        try: 
            object.ovn = object.ovn + 1
            object.updated_date = datetime.utcnow
            object.updated_by = current_user.id
            object.is_active = 'F'
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

class User(BaseMixin, UserMixin):
    __tablename__ = 'xxart_user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(length=100), unique=True, nullable=False)
    email = db.Column(db.String(length=300), unique=True, nullable=False)
        
class Role(BaseWho):
    __tablename__ = 'xxart_role'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=100), unique=True, nullable=False)
    description = db.Column(db.String(length=200), nullable=True)
    
    
class UserRole(BaseMixin):
    __tablename__ = 'xxart_user_role'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('xxart_user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('xxart_role.id'), nullable=True)
    