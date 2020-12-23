from flask import Blueprint, jsonify, request
from .models import db
from .models import *
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
    text = '以下について考えたので買います。'
    for i in range(3):
        key = 'q{}'.format(i)
        qi = data[key]
        text = "%0a".join([text, qi])

    tdict = {'text': text}

    return jsonify(tdict)

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
