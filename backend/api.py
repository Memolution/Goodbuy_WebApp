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

@api.route("/getquestion", methods=["POST"])
def getquestion():
    category_name = request.get_json()['category']

    category_id = db.session.query(Categories.id).\
        filter(Categories.category == category_name).all()[0]

    question_lists = db.session.query(Questionnaire).\
        filter(Questionnaire.category_id == category_id).all()


    question_dict = [question.to_dict() for question in question_lists]

    return jsonify(question_dict)
