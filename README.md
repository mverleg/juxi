
# juxi 🦎

Simple webservice for some testing and deployment automation.

Planned features:

* Trigger (dev) releases based on PRs and manual input
* Take down dev services after a while
* Update DNS records
* Simple monitoring and alerting
* Do regular backups

## Local dev

The first time, you need

* Install dependencies: `pip install .[test]`
* Migrate database: `python3 manage.py migrate`
* Create a `local.py` setting file, example `local.example.py`

Then subsequently, when starting run these two commands in separate shells:

    npm run css-watch
    python3 manage.py runserver

## Release

Create the Docker image

    docker build -t 'mverleg/juxi:latest' .

Test it

    docker run --rm -p5000:5000 -it 'mverleg/juxi:latest'
    
Push if all okay

    docker push 'mverleg/juxi:latest'

