
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
#from operate import test  # 从common包中导入mysql_operate，使用其db

# 创建Flask实例
import settings
from entity.User import User

app = Flask(__name__)

app.config.from_object(settings.Configs)  # 加载flask项目配置

db = SQLAlchemy(app)  # 创建映射对象,并绑定在app中





@app.route("/test", methods=['POST', 'GET'])
def hello():
    print(request)
    respone = {
        "method ": request.method,
        "body": request.json,
        "head": dict(request.headers),
        "data":  request.args
    }
    return respone

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['myFile']
    print(f.filename)
    f.save('./upload_dir/'+f.filename)
    return "file save success"

@app.route('/register', methods=['POST'])
def register():
    mail=request.json['mail']
    print(mail)
    user = User.query.filter_by(mail=mail).all()  # 查询名为huan的数据
    print(user)
    # user1 = User(mail="2083978036@qq.com")  # 创建实例对象
    # db.session.add(user1)  # 插入数据
    # db.session.commit()  # 提交事务
    return ""



# if __name__ == "__main__":
#     # debug=True 代码修改能运行时生效，app.run运行服务
#     # host默认127.0.0.1 端口默认5000
#     app.run(debug=True)




