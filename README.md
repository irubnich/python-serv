# Python Server
This is a really, really basic HTTP server implemented in Python that can serve GET and HEAD requests.

## Features
  - Serves files
  - Deployable to Heroku

## How To Install
1. Clone the repo:

	```sh
    $ git clone git@github.com:irubnich/python-serv.git
    $ cd python-serv
	```

2. Run the server:

	```sh
 	$ ./server.py
    ```

3. Go to `http://localhost:8080` and enjoy.

## Stuff to Load
- `index.html` - simple HTML file
- `doge.png` - an image
- `other_file.ext` - regular file that triggers a browser download

## On Heroku
I deployed this to http://stormy-island-9205.herokuapp.com/ and it serves files remotely as well as it does locally. Give it a few seconds for the dyno to wake up the first time you load the page. This is normal behavior if you have less than 2 dynos.

## Credits
Based on a Ruby tutorial I stumbled upon a while ago: https://practicingruby.com/articles/implementing-an-http-file-server

I took the basic concepts from there and applied them to Python and its TCPServer implementation, while creating some new classes like `Headers` and `Request`.
