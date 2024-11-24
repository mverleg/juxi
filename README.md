
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

    npx tailwindcss -i ./src/tailwind/juxi.css -o ./src/static/juxi.min.css --minify --watch
    flask run --debug

## Release

Create the Docker image

    docker build -t 'mverleg/juxi:latest' .

Test it

    docker run --rm -p5000:5000 -it 'mverleg/juxi:latest'
    
Push if all okay

    docker push 'mverleg/juxi:latest'

