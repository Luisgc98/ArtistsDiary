from app.test import test
from models import User, UserRole, Role
from flask import url_for, redirect , render_template

@test.route('/test', methods=['GET','POST'])
def test():
    
    return render_template('test/test.html')