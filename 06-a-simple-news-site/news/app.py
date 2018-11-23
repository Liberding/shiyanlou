#!/usr/bin env python3
#-*- coding:utf-8 -*-

from flask import Flask, render_template, abort
import os
import json
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

result = {}
directory = os.path.join(os.getcwd(),'..','files')
for i in os.listdir(directory):
    file_path = os.path.join(directory,i)
    with open(file_path) as f:
        result[i[:-5]] = json.load(f)


@app.route('/')
def index():
    l = [i['title'] for i in result.values()]
    print(l)
    return render_template('index.html', l=l)

@app.route('/files/<filename>')
def file(filename):
    f = result.get(filename)
    if not f:
        abort(404)
    return render_template('file.html',f=f)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
