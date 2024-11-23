
# juxi 🦎

Simple webservice for some testing and deployment automation.

Planned features:

* Trigger (dev) releases based on PRs and manual input
* Take down dev services after a while
* Update DNS records
* Simple monitoring and alerting
* Do regular backups

## Local dev


## Release

1. Create the image

   docker build -t 'mverleg/yuxi:latest' -f deploy/Dockerfile deploy
   docker push -t 'mverleg/yuxi:latest' -f deploy/Dockerfile deploy

