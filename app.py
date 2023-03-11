from flask import Flask
import socket
import datetime

app=Flask(__name__)
@app.route('/')

def hello_word():
  hostname= socket.gethostname()
  time = datetime.datetime.now().strftime("%m/%d/%Y,%H:%M:%S")
  return 'Welcome from '+hostname+', at '+time

if __name__ == "__main__":
  app.run('0.0.0.0','5000')
