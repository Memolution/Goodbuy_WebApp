from . import db

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
        return '<TeacherInfo %r, %r>' % self.name


class ScheduleInfo(db.Model):
    __tablename__ = 'schedules'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer,
                        db.ForeignKey(
                            'students.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE')
                        )
    teacher_id = db.Column(db.Integer,
                        db.ForeignKey(
                            'teachers.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE')
                        )
    Mon1 = db.Column(db.Integer)
    Mon2 = db.Column(db.Integer)
    Mon3 = db.Column(db.Integer)
    Mon4 = db.Column(db.Integer)
    Tue1 = db.Column(db.Integer)
    Tue2 = db.Column(db.Integer)
    Tue3 = db.Column(db.Integer)
    Tue4 = db.Column(db.Integer)
    Wed1 = db.Column(db.Integer)
    Wed2 = db.Column(db.Integer)
    Wed3 = db.Column(db.Integer)
    Wed4 = db.Column(db.Integer)
    Thu1 = db.Column(db.Integer)
    Thu2 = db.Column(db.Integer)
    Thu3 = db.Column(db.Integer)
    Thu4 = db.Column(db.Integer)
    Fri1 = db.Column(db.Integer)
    Fri2 = db.Column(db.Integer)
    Fri3 = db.Column(db.Integer)
    Fri4 = db.Column(db.Integer)
    Sat1 = db.Column(db.Integer)
    Sat2 = db.Column(db.Integer)
    Sat3 = db.Column(db.Integer)
    Sat4 = db.Column(db.Integer)
    Sun1 = db.Column(db.Integer)
    Sun2 = db.Column(db.Integer)
    Sun3 = db.Column(db.Integer)
    Sun4 = db.Column(db.Integer)


    def to_dict(self):
        return dict(
            id = self.id,
            student_id = self.student_id,
            teacher_id = self.teacher_id,
            Mon1 = self.Mon1,
            Mon2 = self.Mon2,
            Mon3 = self.Mon3,
            Mon4 = self.Mon4,
            Tue1 = self.Tue1,
            Tue2 = self.Tue2,
            Tue3 = self.Tue3,
            Tue4 = self.Tue4,
            Wed1 = self.Wed1,
            Wed2 = self.Wed2,
            Wed3 = self.Wed3,
            Wed4 = self.Wed4,
            Thu1 = self.Thu1,
            Thu2 = self.Thu2,
            Thu3 = self.Thu3,
            Thu4 = self.Thu4,
            Fri1 = self.Fri1,
            Fri2 = self.Fri2,
            Fri3 = self.Fri3,
            Fri4 = self.Fri4,
            Sat1 = self.Sat1,
            Sat2 = self.Sat2,
            Sat3 = self.Sat3,
            Sat4 = self.Sat4,
            Sun1 = self.Sun1,
            Sun2 = self.Sun2,
            Sun3 = self.Sun3,
            Sun4 = self.Sun4
        )

    def __repr__(self):
        return '<Scheule %r, %r>' % self.id
