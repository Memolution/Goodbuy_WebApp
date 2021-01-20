from flask import Blueprint, jsonify, request
from .models import db
from .models import *
import urllib.parse
import re

# coding: utf-8

api = Blueprint('api', __name__)


@api.route('/hoge/<string:str>', methods=["GET"])
def hogeGet(str):
    return "hogeGet: " + str


@api.route("/hoge", methods=["POST"])
def hogePost():
    text = request.form["text"]
    return "hogePost: " + text


# レコード全取得APIの例
@api.route("/test", methods=["GET"])
def test():
    test_list = db.session.query(Test).all()
    test_dict = [test.to_dict() for test in test_list]
    return jsonify(test_dict)


@api.route("/getcategory", methods=["POST"])
def get_category():
    data = []
    category_list =  db.session.query(Categories.category).all()
    for category in category_list:
        category_dict = {}
        category_dict['label'] = category[0]
        category_dict['value'] = category[0]
        data.append(category_dict)

    return jsonify(data)


@api.route("/getquestion", methods=["POST"])
def get_question():
    category_name = request.get_json()['category']

    category_id = db.session.query(Categories.id).\
        filter(Categories.category == category_name).all()[0]

    question_lists = db.session.query(Questionnaire).\
        filter(Questionnaire.category_id == category_id).all()


    question_dict = [question.to_dict() for question in question_lists]

    return jsonify(question_dict)


@api.route("/geturl", methods=["POST"])
def get_url():
    try:
        current_url = request.get_json()['url']
        url_dict = {'current_url': current_url}
    except TypeError:
        no_url = {'current_url': ''}
        return jsonify(no_url)

    return jsonify(url_dict)


@api.route("/question_to_tweet", methods=["POST"])
def conversion_tweet():
    data = request.get_json()['question']
    original_url = request.get_json()['url'][0]

    base = 'https://www.amazon.co.jp'
    pattern = r'/dp\/.+/'
    shorten = re.search(pattern, original_url)

    shorten_url = base + shorten.group()

    text = '以下について考えたので買います。'
    for i in range(4):
        key = 'q{}'.format(i)
        qi = data[key]
        text = "%0a".join([text, qi])

    # text = text.replace('\n', '')
    base_url = 'https://twitter.com/intent/tweet?hashtags=Goodbuy_enp&text='
    first_html_tag = '<a href="'
    latter_html_tag = '"target="_blank" rel="noopener noreferrer">ツイートする</a>'
    url = first_html_tag + base_url + text + shorten_url + latter_html_tag
    urldict = {'url': url}

    return jsonify(urldict)


@api.route("/content_to_tweet", methods=["POST"])
def conversion_url():
    data = request.get_json()['tweet']['content']
    original_url = request.get_json()['tweet']['url']

    # https://www.amazon.co.jp/dp/4798163686/ これを目標にする
    # dp/商品コード10桁　
    base = 'https://www.amazon.co.jp'
    pattern = r'/dp\/.+/'
    shorten = re.search(pattern, original_url)

    shorten_url = base + shorten.group()

    data = data.replace('\n', '')
    base_url = 'https://twitter.com/intent/tweet?hashtags=Goodbuy_enp&text='
    first_html_tag = '<a href="'
    latter_html_tag = '"target="_blank" rel="noopener noreferrer">ツイートする</a>'
    url = first_html_tag + base_url + data + '%0a' + shorten_url + latter_html_tag

    urldict = {'url': url}

    return jsonify(urldict)


# ざっくりユーザー新規登録API
@api.route("/registration", methods=["POST"])
def new_regstration():
    if "name" in request.form:
        user_name = request.form["name"]
    else:
        return "error: not found name"

    if len(db.session.query(R_user.user_name).filter(
            R_user.user_name == user_name).all()) != 0:
        return "this user name is exist"

    if "email" in request.form:
        user_email = request.form["email"]
    else:
        return "error: not found email"

    if len(db.session.query(R_user.user_name).filter(
            R_user.e_mail == user_email).all()) != 0:
        return "this email address is exist"

    if "password" in request.form:
        password = request.form["password"]
    else:
        return "error: not found password"

    user_data = [R_user(
        e_mail=user_email,
        user_name=user_name,
        password=password
    )]

    db.session.add_all(user_data)
    db.session.commit()

    return "complete registration"


# ざっくりlogin認証
@api.route("/login", methods=["POST"])
def login():
    user_email = ""
    password = ""
    if "email" in request.form:
        user_email = request.form["email"]
    else:
        return "error: not found email"

    if "password" in request.form:
        password = request.form["password"]
    else:
        return "error: not found password"

    user_name = db.session.query(
        R_user.user_name).filter(
        R_user.e_mail == user_email,
        R_user.password == password).all()
    if len(user_name) == 0:
        return "permission denied"

    user_name = user_name[0][0]
    return str(user_name)



@api.route("/line", methods=["POST"])
def post_line():
    data = request.get_json()['line']['message']

    message = urllib.parse.quote(data)

    base_url = 'https://line.me/R/msg/text/?'
    first_html_tag = '<a href="'
    latter_html_tag = '"target="_blank" rel="noopener noreferrer">Lineに保存</a>'
    url = first_html_tag + base_url + message + latter_html_tag

    urldict = {'url': url}

    return jsonify(urldict)


@api.route("/visitCount", methods=["POST"])
def level_up():
    degree = ['初心者', '見習い', '駆け出し', '修行中', '一人前', '玄人', '名人', '鉄人', '達人', '大達人', '神']
    visit_count = request.get_json()['visitCount']['count']
    current_level = int(visit_count / 5)
    previous_level = current_level - 1
    if current_level >= len(degree):
        message = {'message':'いい買い物習慣の神の域です!'}
    else:
        if previous_level < 0:
            comment = 'あなたはいい買い物習慣の初心者です。どんどんこのアプリを使っていい買い物習慣を作っていきましょう！'
        else:
            comment = 'おめでとうございます.\nあなたはいい買い物習慣{0}から{1}に上達しました'.format(degree[previous_level], degree[current_level])
        message = {'message': comment}

    return jsonify(message)


@api.route("/viewLevel", methods=["POST"])
def view_level():
    degree = ['初心者', '見習い', '駆け出し', '修行中', '一人前', '玄人', '名人', '鉄人', '達人', '大達人', '神']
    visit_count = request.get_json()['visitCount']['count']
    current_level = int(visit_count / 5)
    times = 5 - int(visit_count % 5)

    if current_level >= len(degree):
        message = {'message':'いい買い物習慣の神の域です!'}
    else:
        comment = 'いい買い物習慣のレベルはずばり{0}です！\n あと{1}回購入理由を考えると買い物習慣が上達します！'.format(degree[current_level], times)
        message = {'message': comment}

    return jsonify(message)
