import os

from flask import Flask, render_template

from views.auth import build_auth


def create_app(test_config=None):
    app = Flask('juxi',
        template_folder='templates',
        static_url_path='/s',
        static_folder='static/',
        instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'juxi.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    build_auth(app)
    @app.route('/')
    def home():
        return render_template('index.html')


    return app


if __name__ == '__main__':
    create_app().run(debug=True)

