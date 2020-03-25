from flask import Flask, render_template, redirect, request, url_for, jsonify
import data_handler
import engine

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def route_game():
    data = data_handler.create_json_data()
    return render_template('game.html', data=data)


@app.route('/game-data')
def route_game_data():
    data = data_handler.create_json_data()
    return jsonify(data)


@app.route('/user-input/<userinput>')
def route_user_input(userinput):
    engine.dealBoard(userinput)


@app.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    jsdata = request.form['answer']
    print(jsdata)
    return jsdata


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
