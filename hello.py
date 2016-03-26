from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from goty_winners import GOTY_WINNERS

app = Flask(__name__)
bootstrap = Bootstrap(app)

def get_games(source):
    games = []
    for row in source:
        game = row["Game"]
        games.append(game)
    return sorted(games)

def get_gamedata(source, game):
    for row in source:
        if game == row["Game"]:
            dev = row["Developer"].decode('utf-8')
            year = row["Year"]
    return game, dev, year

@app.route('/winners')
def home():
    games = get_games(GOTY_WINNERS)
    return render_template('index.html', games=games)

@app.route('/winners/<game>')
def details(game):
    game, dev, year = get_gamedata(GOTY_WINNERS, game)
    return render_template('details.html', game=game, dev=dev, year=year)

if __name__ == '__main__':
    app.run()
