from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Week 3 Day 3 Debug Pipeline</h1>'

@app.route('/health')
def health():
    return jsonify({'healthy': True, 'service': 'week3-debug'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
