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
            category = "日用品・生活雑貨" #id = 1
        ),
        Categories(
            category = "本・電子書籍" #id = 2
        ),
        Categories(
            category = "ファッション・小物" #id = 3
        ),
        Categories(
            category = "スポーツ・アウトドア" #id = 4
        ),
        Categories(
            category = "コスメ・健康・医薬品" #id = 5
        ),
        Categories(
            category = "ゲーム" #id = 6
        ),
        Categories(
            category = "家電・PC" #id = 7
        ),
        Categories(
            category = "食品・スイーツ・お酒" #id = 8
        ),
        Categories(
            category = "インテリア・寝具" #id = 9
        ),
        Categories(
            category = "その他" #id = 10
        ),
    ]
    db.session.add_all(category_list)
    db.session.commit()


    db.session.query(Questionnaire).delete()


    # category_id は上のカテゴリーの並んでる順に対応（日用雑貨が1）
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
            content = "デパートで試してから買えば？"
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
        Questionnaire(
            category_id = 7,
            content = "性能比較した？"
        ),
        Questionnaire(
            category_id = 7,
            content = "今あるやつ壊れてからにしたら？"
        ),
        Questionnaire(
            category_id = 7,
            content = "もう少し待てばいいスペック出るかもよ？"
        ),
        Questionnaire(
            category_id = 8,
            content = "近所のチラシと値段比較した？"
        ),
        Questionnaire(
            category_id = 8,
            content = "カロリー大丈夫？"
        ),
        Questionnaire(
            category_id = 8,
            content = "健康を考慮した？"
        ),
        Questionnaire(
            category_id = 9,
            content = "置く場所ちゃんとある？"
        ),
        Questionnaire(
            category_id = 9,
            content = "今もってない？"
        ),
        Questionnaire(
            category_id = 9,
            content = "全体の雰囲気にちゃんとあってる？"
        ),
        Questionnaire(
            category_id = 10,
            content = "最近買ったばかりじゃない？"
        ),
        Questionnaire(
            category_id = 10,
            content = "今すぐ必要？"
        ),
        Questionnaire(
            category_id = 10,
            content = "他のと比較した？"
        ),
    ]
    db.session.add_all(questionnaire_list)
    db.session.commit()


    user_list = [
    #passwordは'pass'をハッシュ化したもの
        User(
                user_name='Shindo',
                e_mail='test1@example.com',
                password='93329c60badb9d8252ad6c9d5f0c07f1848948bc5bd4b42ad9301a90639e8880'
            ),
        User(
                user_name='Futami',
                e_mail='test2@example.com',
                password='93329c60badb9d8252ad6c9d5f0c07f1848948bc5bd4b42ad9301a90639e8880'
            ),
        User(
                user_name='R.Sato',
                e_mail='test3@example.com',
                password='93329c60badb9d8252ad6c9d5f0c07f1848948bc5bd4b42ad9301a90639e8880'
            ),
        User(
                user_name='Y.Sato',
                e_mail='test4@example.com',
                password='93329c60badb9d8252ad6c9d5f0c07f1848948bc5bd4b42ad9301a90639e8880'
            ),
        User(
                user_name='Matsuda',
                e_mail='test5@example.com',
                password='93329c60badb9d8252ad6c9d5f0c07f1848948bc5bd4b42ad9301a90639e8880'
            ),
        User(
                user_name='Watanabe',
                e_mail='test6@example.com',
                password='93329c60badb9d8252ad6c9d5f0c07f1848948bc5bd4b42ad9301a90639e8880'
            ),
    ]
    db.session.add_all(user_list)
    db.session.commit()
