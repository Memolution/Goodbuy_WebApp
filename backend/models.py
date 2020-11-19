from . import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

# create user 'mysql'@'localhost' identified by 'pass';
# create database shigakusha;
# grant all on shigakusha.* to mysql@localhost;
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


# class User(db.Model):
#     __tablename__ = 'users'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(100))
#     e_mail = db.Column(db.String(100))
#     password = db.Column(db.String(100))

#     def to_dict(self):
#         return dict(
#             id=self.id,
#             user_name=self.user_name,
#             e_mail=self.e_mail,
#             password=self.password
#         )

#     def __repr__(self):
#         return '<User %r>' % self.user_name


# class Todo(db.Model):
#     __tablename__ = 'todolists'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer,
#                         db.ForeignKey(
#                             'users.id',
#                             onupdate='CASCADE',
#                             ondelete='CASCADE')
#                         )
#     title = db.Column(db.String(100))
#     content = db.Column(db.String(1000))
#     start_date = db.Column(db.DateTime)
#     end_date = db.Column(db.DateTime)
#     image_name = db.Column(db.String(100))
#     done_flag = db.Column(db.Integer)
#     priority_flag = db.Column(db.Integer)

#     def to_dict(self):
#         return dict(
#             id = self.id,
#             user_id = self.user_id,
#             title = self.title,
#             content = self.content,
#             start_date = self.start_date,
#             end_date = self.end_date,
#             image_name = self.image_name,
#             done_flag = self.done_flag,
#             priority_flag = self.priority_flag
#         )

#     def __repr__(self):
#         return '<Todo %r, %r>' % self.name


# class PurchasedList(db.Model):
#     __tablename__ = 'purchasedlists'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer,
#                         db.ForeignKey(
#                             'users.id',
#                             onupdate='CASCADE',
#                             ondelete='CASCADE')
#                         )
#     title = db.Column(db.String(100))
#     content = db.Column(db.String(1000))
#     price = db.Column(db.Integer)
#     image_name = db.Column(db.String(100))
#     again_flag = db.Column(db.Integer)
#     reputation = db.Column(db.Integer)


#     def to_dict(self):
#         return dict(
#             id = self.id,
#             user_id = self.user_id,
#             title = self.title,
#             content = self.content,
#             price = self.price,
#             image_name = self.image_name,
#             again_flag = self.again_flag,
#             reputation = self.reputation
#         )

#     def __repr__(self):
#         return '<PurchasedList %r, %r>' % self.name


# class ReadList(db.Model):
#     __tablename__ = 'purchasedlists'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer,
#                         db.ForeignKey(
#                             'users.id',
#                             onupdate='CASCADE',
#                             ondelete='CASCADE')
#                         )
#     title = db.Column(db.String(100))
#     content = db.Column(db.String(1000))
#     author = db.Column(db.String(100))


#     def to_dict(self):
#         return dict(
#             id = self.id,
#             user_id = self.user_id,
#             title = self.title,
#             content = self.content,
#             author = self.author
#         )

#     def __repr__(self):
#         return '<ReadList %r, %r>' % self.name

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