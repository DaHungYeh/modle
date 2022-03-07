# -*- coding: UTF-8 -*-
from app import app

print('hello')

@app.route('/')
def index():
    return 'Flask API started'


if __name__ == "__name__":
    app.run(host='0.0.0.0', porn=3000, debug=True)