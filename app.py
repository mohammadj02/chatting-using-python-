from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/<username>')
def user_chat(username):
    if username not in ['user1', 'user2']:
        return "Invalid user", 404
    return render_template('chat.html', username=username)

@socketio.on('message')
def handleMessage(data):
    print(f"Received message from {data['sender']}: {data['msg']}")
    send(data, broadcast=True)

if __name__ == '__main__':
    # The host '0.0.0.0' makes the server accessible network-wide
    # Default port is 5000, can be changed if needed
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
