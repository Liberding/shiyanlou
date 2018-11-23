#!/usr/bin env python3
#-*- coding:utf-8 -*-

from flask import Flask, render_template, abort
import os
import json

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.comfig['SQLALCHEMY_DATABASE_URI'] = 'mysql:root@localhost/shiyanlou'





@app.route('/')
def index():
    pass
    return render_template('index.html', l=l)

@app.route('/files/<filename>')
def file(file_id):
    
    if not f:
        abort(404)
    return render_template('file.html',f=f)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
