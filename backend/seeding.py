from . import db
from .models import *
# coding: utf-8

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

    db.session.add_all(test_list)
    db.session.commit()


    db.session.query(Categories).delete()
    category_list = [
        Categories(
            category = "日用品・生活雑貨"
        ),
        Categories(
            category = "本"
        ),
        Categories(
            category = "ファッション・小物"
        ),
        Categories(
            category = "スポーツ・アウトドア"
        ),
        Categories(
            category = "コスメ"
        ),
        Categories(
            category = "ゲーム"
        ),
        Categories(
            category = "その他"
        ),
    ]
    db.session.add_all(category_list)
    db.session.commit()


    db.session.query(Questionnaire).delete()

    questionnaire_list = [
        Questionnaire(
            category_id = 1,
            content = "ストック多すぎない？"
        ),
        Questionnaire(
            category_id = 1,
            content = "今すぐ必要？"
        ),
        Questionnaire(
            category_id = 1,
            content = "スーパーにもっと安いのない？"
        ),
        Questionnaire(
            category_id = 2,
            content = "積読にならない？"
        ),
        Questionnaire(
            category_id = 2,
            content = "その本読んで得られるものある？"
        ),
        Questionnaire(
            category_id = 2,
            content = "似たような本持ってない？"
        ),
        Questionnaire(
            category_id = 3,
            content = "最近買ったばっかりじゃない？"
        ),
        Questionnaire(
            category_id = 3,
            content = "セールまで待てば？"
        ),
        Questionnaire(
            category_id = 3,
            content = "素材とか気にした？"
        ),
        Questionnaire(
            category_id = 4,
            content = "ほんとに使う予定ある？"
        ),
        Questionnaire(
            category_id = 4,
            content = "似たようなの持ってない？"
        ),
        Questionnaire(
            category_id = 4,
            content = "セールまで待てば？"
        ),
        Questionnaire(
            category_id = 5,
            content = "新作だから買おうとしてない？"
        ),
        Questionnaire(
            category_id = 5,
            content = "最近買ったばっかりじゃない？"
        ),
        Questionnaire(
            category_id = 5,
            content = "デパ地下で試してから買えば？"
        ),
        Questionnaire(
            category_id = 6,
            content = "新作だから買おうとしてない？"
        ),
        Questionnaire(
            category_id = 6,
            content = "積みゲー多くない？"
        ),
        Questionnaire(
            category_id = 6,
            content = "一緒にやる人いる？"
        ),
    ]
    db.session.add_all(questionnaire_list)
    db.session.commit()
