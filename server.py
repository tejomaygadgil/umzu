from flask import Flask
from flask_socketio import SocketIO
import os
import threading
import wozu

app = Flask(__name__)
socketio = SocketIO(app)


def monitor_file():
    files = ["graph.txt", "links.txt", "todo.txt"]
    last_modified_times = {file: os.path.getmtime(file) for file in files}

    while True:
        for file in files:
            current_modified_time = os.path.getmtime(file)
            if current_modified_time > last_modified_times[file]:
                last_modified_times[file] = current_modified_time
                socketio.emit("file_updated", {"file": file}, namespace="/")


@app.route("/")
def index():
    html = wozu.generate_html()
    return html


if __name__ == "__main__":
    threading.Thread(target=monitor_file, daemon=True).start()
    socketio.run(app, host="127.0.0.1", port=5000)
