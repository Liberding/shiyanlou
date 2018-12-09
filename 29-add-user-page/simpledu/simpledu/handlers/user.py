from flask import Blueprint, render_template
from simpledu.models import User
from simpledu.models import Course
user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<user_name>')
def index(user_name):
    users = User.query.filter_by(username=user_name).first_or_404()
    courses = Course.query.all()
    return render_template('detail.html', users=users, courses=courses)
