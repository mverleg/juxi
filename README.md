
# juxi 🦎

Simple webservice for some testing and deployment automation.

Planned features:

* Trigger (dev) releases based on PRs and manual input
* Take down dev services after a while
* Update DNS records
* Simple monitoring and alerting
* Do regular backups

## Local dev

Install dependencies like flask in a virtualenv with `pip install .`, and run

    flask run --debug

## Release

Create the image

    docker build -t 'mverleg/yuxi:latest' .

Test it

    docker run --rm -p5000:5000 -it 'mverleg/yuxi:latest'
    
Push if all okay

    docker push 'mverleg/yuxi:latest'

