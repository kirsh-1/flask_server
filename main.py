from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    send(f'User {data["username"]} joined room {room}.', room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    send(f'User {data["username"]} left room {room}.', room=room)

@socketio.on('message')
def handle_message(data):
    send(data, room=data['room'])

if __name__ == "__main__":
    socketio.run(app, host='192.168.0.108', debug=True)