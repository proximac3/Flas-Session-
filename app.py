from werkzeug.datastructures import ContentSecurityPolicy
from werkzeug.wrappers import response
from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
import json
app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'inkudio'
boggle_game = Boggle()


@app.route('/game')
def generate_game_board():
    """"Ganerate game board and redner template"""

    game_board = boggle_game.make_board()
    session['game_board'] = game_board

    return render_template('game_board.html', game_board=game_board)


@app.route('/words', methods=['POST'])
def checkForWord():
    """Check if submitted word is valid and respond with Json file"""

    check_word_in_words = boggle_game.check_valid_word(session['game_board'], 
        request.json.get('word'))

    results = {'results': check_word_in_words}

    return jsonify(results)


@app.route('/update', methods=['POST'])
def update_game():
    """ Update User High And Number of times Game has been played"""

    highscore = request.json.get('high Score')
    times_played = request.json.get('times played')
    # Check if received high score is greater than previous high score and update it.
    try:
        if session['high score']:
            if int(highscore) > session['high score']:
                session['high score'] = int(highscore)
    except:
        print('session does not exist')
        session['high score'] = session.get('high score', 0) + int(highscore)

    session['# of games played'] = session.get('# of games played', 0) + int(times_played)

    results = {
        'High Score': session['high score'],
        '# of games played': session['# of games played']
    }

    print(session['game_board'])

    return jsonify(results)


@app.route('/session')
def session_data():
    """Return Session Data"""
    
    return str(session['game_board'])