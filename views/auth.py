from flask import render_template

def build_auth(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('login.html')

    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        return render_template('logout.html')

