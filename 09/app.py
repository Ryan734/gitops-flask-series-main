import os  # new
from flask import Flask 

app = Flask(__name__)

name = os.getenv("NAME", "service1")  # new
cluster_name = os.getenv("CLUSTER", "cluster1")  # new


@app.route('/')
def hello():
    return 'hello'


# new
@app.route('/cluster')
def cluster():
    return f'This is {name} in cluster {cluster_name}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
