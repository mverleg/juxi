
from flask import Flask, render_template

def build_urls(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('login.html')

    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        return render_template('logout.html')

    @app.route('/')
    def home():
        return render_template('index.html')
