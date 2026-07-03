from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/count")
def count():
    visits = redis_client.incr("visits")
    return render_template("count.html", visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
