# Python Server
This is a really, really basic HTTP server implemented in Python that can serve GET and HEAD requests.

## Features
  - Serves files
  - Deployable to Heroku

## How To Install
1. Clone the repo:

  `$ git clone git@github.com:irubnich/python-serv.git`
  `$ cd python-serv`

2. Run the server:

  `$ ./server.py`

3. Go to `http://localhost:8080` and enjoy.

## Stuff to Load
- `index.html` - simple HTML file
- `doge.png` - an image
- `other_file.ext` - regular file that triggers a browser download

## On Heroku
I deployed this to http://stormy-island-9205.herokuapp.com/ and it serves files remotely as well as it does locally.
