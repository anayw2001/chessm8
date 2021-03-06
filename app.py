from flask import Flask, render_template, request
import chess
import lichess
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')
        
@app.route('/chesscom', methods=['GET','POST'])
def chessdotcom():
    if request.method == "POST":
        player = request.form['player']
        if chess.test_username(player):
            win_stats = chess.ret_nice(chess.get_win_stats(player))
            ratings = chess.get_ratings(player)
            title = chess.get_title(player)
            return render_template('result.html', player=player, title=title, ratings_arr=ratings, winstats=win_stats)
        else:
            return render_template('error.html')

@app.route('/lichess', methods=['GET','POST'])
def lichess():
    if request.method == "POST":
        player = request.form['player']
        if lichess.test_username(player):
            win_stats = lichess.ret_nice(lichess.get_win_stats(player))
            ratings = lichess.get_ratings(player)
            title = lichess.get_title(player)
            return render_template('result.html', player=player, title=title, ratings_arr=ratings, winstats=win_stats)
        else:
            return render_template('error.html')

# @app.route('/user')


if __name__ == '__main__':
    app.run()
