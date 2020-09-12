from . import db
from .models import Test, StudentInfo, TeacherInfo, ScheduleInfo


def seed():
    # テーブルのデータを消去
    db.session.query(Test).delete()

    # 初期データを追加
    test_list = [
        Test(
            id=1,
            text="text_1",
            number=10
        ),
        Test(
            id=2,
            text="text_2",
            number=100
        )
    ]

    students_list = [
        StudentInfo(
            number=P1,
            name='滝本和奏',
            school='常総学院高校',
            year='h3'
        ),
        StudentInfo(
            number=P2,
            name='滝本和奏',
            school='常総学院高校',
            year='h3'
        ),
        StudentInfo(
            number=P3,
            name='滝本和奏',
            school='常総学院高校',
            year='h3'
        ),
        StudentInfo(
            number=P4,
            name='滝本和奏',
            school='常総学院高校',
            year='h3'
        ),
        StudentInfo(
            number=P5,
            name='滝本和奏',
            school='常総学院高校',
            year='h3'
        )

    ]

    db.session.add_all(test_list)

    db.session.commit()
