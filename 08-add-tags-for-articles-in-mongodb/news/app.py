#!/usr/bin env python3
#-*- coding:utf-8 -*-
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)

mongodb = client.shiyanlou_mongo

app = Flask(__name__)

#app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.update(dict(SQLALCHEMY_DATABASE_URI='mysql://root@localhost/shiyanlou',SQLALCHEMY_TRACK_MODIFICATIONS=False))

db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', uselist=False)
    content = db.Column(db.Text)
    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    # 向文章添加标签
    def add_tag(self, tag_name):
        # 为当前文章添加 tag_name 标签存入到 MongoDB
        pass
    ＃移出标签
    def remove_tag(self, tag_name):
        # 从 MongoDB 中删除当前文章的 tag_name 标签
        pass

    # 标签列表
    @property
    def tags(self):
        # 读取 mongodb 返回当前文章的标签列表

        pass
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')
    def __init__(self, name):
        self.name = name
        
def insert_datas():
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
@app.route('/')
def index():
    return render_template('index.html', files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html',file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
