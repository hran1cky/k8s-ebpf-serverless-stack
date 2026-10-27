import os
import redis
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

REDIS_HOST = os.environ.get("REDIS_HOST", "redis-db")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

@app.route('/api/stats')
def get_stats():
    visits = r.incr('visits')
    return jsonify({
        "status": "online",
        "visits": visits,
        "message": "Aplikacia bezi uspesne v Docker kontajneri!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)