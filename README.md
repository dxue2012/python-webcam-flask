This is a toy project for learning how to use a couple of python libraries. 

### Repo status

This repo is **unmaintained**. I guess I never intended for others to use this (and never imagined my terrible code would be of any value to others), but I recognize that a nonzero number of people have stumbled upon this repo and may have found it useful as a reference.
Given that, even though I do not plan on maintaining this repo, I am happy for people to 

1) submit pull requests to fix known issues (there are quite a few), or to 
2) fork and make your own version. I'd be happy to link to a better maintained fork for future readers' benefit.

### What it does

1) The web client sends video stream data (from the user's webcam) to a flask server using socketio
2) The server does some processing on the video stream
3) The client receives the processed video stream and re-displays the results in a different frame

In the demo site, the server is simply flipping the image horizontally. You could imagine it doing something more sophisticated (e.g. applying some filters), but obviously I was too lazy to implement anything cool.

### Known issues

- The server does not handle multiple clients well. If multiple clients connect, the server treats them as one and sends back mixed frames as a result.

### Demo
[Live Demo](https://python-stream-video.herokuapp.com)

### Setup

#### Optional

- setup heroku (`brew install heroku`)
- Use a python virtualenv

#### Required
- `git clone https://github.com/dxue2012/python-webcam-flask.git`
- `pip install -r requirements.txt`

### Run locally

IF YOU HAVE HEROKU:
- `heroku local`
IF NOT:
- `gunicorn -k eventlet -w 1 app:app --log-file=-`

- in your browser, navigate to localhost:5000

### Deploy to heroku

- `git push heroku master`
- heroku open

### Common Issues

If you run into a 'protocol not found' error, see if [this stackoverflow answer helps](https://stackoverflow.com/questions/40184788/protocol-not-found-socket-getprotobyname).
