

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

### Demo
[Live Demo](https://python-stream-video.herokuapp.com)
