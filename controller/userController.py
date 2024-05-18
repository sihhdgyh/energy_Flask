
from flask import Blueprint, request
from sqlalchemy import and_

from database import db
from entity.heart import Heart
from forecast import predictSingle
from mail import sendSMS
from result import result

userController = Blueprint('userController', __name__)

@userController.route('/insertData', methods=['POST'])
def insertData():
    hearts = request.json['heartRate']
    userId=request.json['userId']
    heart =Heart(userId=userId,heart=hearts[-1])

    db.session.add(heart)  # 插入数据
    db.session.commit()  # 提交事务
    modelName = 'test'
    results = 0
    #results=predictSingle(modelName, hearts)
    result1 = result(code=200, data=str(results), msg='成功')
    return result.jsonformat(result1)








