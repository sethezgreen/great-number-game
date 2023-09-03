from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
import random

# root route
@app.route('/')
def root():
    session['total_guesses'] = 0
    session['number'] = random.randint(1,100)
    print ("$$$$$$$$$$$$$$$$$", session['number'])
    return render_template('index.html')

# determines if guess was right or wrong
@app.route('/game', methods=["POST"])
def game():
    session['total_guesses'] += 1
    session['guess'] = int(request.form['guess'])
    if session['guess'] != session['number']:
        if session['total_guesses'] < 5:
            if session['guess'] > session['number']:
                response = "high"
            if session['guess'] < session['number']:
                response = "low"
        else:
            response = "you_lose"
    elif session['guess'] == session['number']:
            response = "correct"
    print(session)
    return render_template('index.html', response=response)

# play again route
@app.route('/play_again')
def play_again():
    session.pop('number')
    session.pop('guess')
    session.pop('total_guesses')
    return redirect('/')

# saves winning players
@app.route('/player/save', methods=["POST"])
def player_save():
    if 'player' not in session:
        session['player'] = {}
    session['player'][request.form['name']] = session['total_guesses']
    return render_template("index.html", response='correct')

# leaderborad route
@app.route('/leaderboard')
def leaderboard():
    player = session['player']
    return render_template("leaderboard.html", player=player)

if __name__ == "__main__":
    app.run(debug=True)


    # session {
        # number : 50
        # player : {Seth:2}
    # }