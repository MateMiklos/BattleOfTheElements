from flask import Flask, render_template, redirect, url_for, jsonify
import data_handler

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def route_game():
    return render_template('game.html')


@app.route('/game-data')
def route_game_data():
    data = data_handler.create_json_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
