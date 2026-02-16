from flask import Flask
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

# custom metric
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total number of requests to the app'
)

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Kubernetes CI/CD + Monitoring POC Running 🚀"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
