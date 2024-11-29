from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

database = SQLAlchemy()
class Task(database.Model):
    id = database.Column(database.Integer, primary_key=True) #这一栏是任务的id号码
    name = database.Column(database.String(120), nullable=False) #这一栏用于存储用户设置的任务名称
    deadline = database.Column(database.DateTime, nullable=False, default=lambda: datetime() + timedelta(minutes=30)) #这一栏用于存储用户设置的ddl，默认为当前时间+30分钟
    tag_color = database.Column(database.Integer, default=0) #我们使用整数来表示已经预设好的若干种颜色。
    details = database.Column(database.Text, nullable=True) #这一栏用于存储用户设置的细节信息。

class Messages(database.Model):
    id = database.Column(database.Integer, primary_key=True) #聊天编号，html按照编号依次显示历史聊天记录
    ## Todo: Sender
    ## Todo: Receiver
    sendtime = database.Column(database.DateTime, nullable=False) 
    text = database.Column(database.Text, nullable=False) #聊天的内容
    #这一栏用于存储用户设置的ddl，默认为当前时间+30分钟