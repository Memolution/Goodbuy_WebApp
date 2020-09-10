from . import db

# create user 'mysql'@'localhost' identified by 'pass';
# create database tabiluck;
# grant all on tabiluck.* to mysql@localhost;
# from backend.models import init
# init()

# def init():
#     db.create_all()


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


class StudentInfo(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    school = db.Column(db.String(100))
    year = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    phone_number = db.Column(db.Integer)
    note = db.Column(db.String(100))

    def to_dict(self):
        return dict(
            id = self.id,
            number = self.number,
            name = self.name,
            school = self.school,
            year = self.yaer,
            subject = self.subject,
            phone_number = self.phone_number,
            note = self.note
        )

    def __repr__(self):
        return '<StudentInfo %r, %r>' % self.name


class TeacherInfo(db.Model):
    __tablename__ = 'teachers'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    subject_flag = db.Column(db.String(100))
    major_flag = db.Column(db.Integer)


    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            subject_flag = self.subject_flag,
            major_flag = self.major_flag
        )

    def __repr__(self):
        return '<StudentInfo %r, %r>' % self.name
