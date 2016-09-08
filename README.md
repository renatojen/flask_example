# flask_example
Python + Flask website example

To use this with passenger:
- create a 'public' folder in the root dir of the application and put the 'static' folder inside it
- create a 'tmp' folder in the root dir of the application
- rename flask_example.py to passenger_wsgi.py
- after deploy, create a 'restart.txt' inside 'tmp' folder

Live example using passenger:
http://flask.renatojensen.com/
