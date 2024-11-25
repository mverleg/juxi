from flask import render_template

from flask import request


def build_auth(app):
    @app.route('/login/', methods=['GET'])
    def login():
        next = request.args.get('next', None)
        return render_template('login.html', next=next)

    @app.route('/login/', methods=['POST'])
    def login_submit():
        return render_template('login.html')

    @app.route('/logout/', methods=['GET'])
    def logout():
        next = request.args.get('next', None)
        return render_template('logout.html', next=next)

    @app.route('/logout/', methods=['POST'])
    def logout_submit():
        return render_template('logout.html')


