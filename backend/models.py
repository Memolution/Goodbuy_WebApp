from . import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

# create user 'mysql'@'localhost' identified by 'pass';
# create database lifehack;
# grant all on lifehack.* to mysql@localhost;
# from backend.models import init
# init()

def init():
    db.create_all()


class Test(db.Model):
    __tablename__ = 'tests'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    number = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id=self.id,
            text=self.text,
            number=self.number
        )

    def __repr__(self):
        return '<Test %r, %r, %r>' % self.id, self.text, self.number


class Categories(db.Model):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))


    def to_dict(self):
        return dict(
            id = self.id,
            category = self.category
        )

    def __repr__(self):
        return '<Category %r, %r>' % self.category

class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer,
                        db.ForeignKey(
                            'categories.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE')
                        )
    content = db.Column(db.String(1000))


    def to_dict(self):
        return dict(
            id = self.id,
            category_id = self.category_id,
            content = self.content
        )

    def __repr__(self):
        return '<ReadList %r, %r>' % self.content

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    e_mail = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def to_dict(self):
        return dict(
            id=self.id,
            user_name=self.user_name,
            e_mail=self.e_mail,
            password=self.password
        )

    def __repr__(self):
        return '<User %r>' % self.user_name

class Post(db.Model):
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey(
                            'users.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE')
                        )
    will = db.Column(db.String(1000))
    posted_date = db.Column(db.Date)

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            will=self.will,
            posted_date=self.posted_date
        )

    def __repr__(self):
        return '<User %r>' % self.user_id
