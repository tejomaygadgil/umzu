import webbrowser
from flask import Flask
from flask_socketio import SocketIO
import os
import time
import threading
import wozu

app = Flask(__name__)
socketio = SocketIO(app)


def monitor_file():
    files = ["graph.txt", "links.txt", "todo.txt"]
    last_modified_times = {file: os.path.getmtime(file) for file in files}

    while True:
        time.sleep(5)
        for file in files:
            try:
                current_modified_time = os.path.getmtime(file)
            except FileNotFoundError:
                pass
            if current_modified_time > last_modified_times[file]:
                last_modified_times[file] = current_modified_time
                socketio.emit("file_updated", {"file": file}, namespace="/")


@app.route("/")
def index():
    html = wozu.generate_html()
    return html

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Thread(target=monitor_file, daemon=True).start()
    threading.Timer(1, open_browser).start()
    socketio.run(app, host="127.0.0.1", port=5000)
