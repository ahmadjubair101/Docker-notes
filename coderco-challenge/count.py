from flask import Flask  # type: ignore[import]
import redis  # type: ignore[import]
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def welcome():
    return "Welcome to the CoderCo Container Challenge!"

@app.route('/count')
def count():
    count = redis_client.incr('visits')
    return f'This page has been visited {count} times.'



if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
