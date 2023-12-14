from flask import Flask, render_template
import logging 

import wozu

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)

@app.route('/')
def index():
    html = wozu.generate_html()
    return html

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)
