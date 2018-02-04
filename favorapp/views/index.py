from flask import render_template, Blueprint

bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/')
def show():
       # return "Hello World"
        return render_template('user.html')