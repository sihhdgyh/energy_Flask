from datetime import datetime

from database import db


class Heart(db.Model):
    # 设置表名
    __tablename__ = 'heart'
    # 创建数据库表字段
    # db.Column(类型，约束)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId=db.Column(db.String(255))
    heart=db.Column(db.Integer)
    timeData = db.Column(db.DateTime, default=datetime.now)
