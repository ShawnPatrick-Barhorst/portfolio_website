from flask import Flask, render_template

app = Flask(__name__)

posts = [

    {
        'title': 'StreetFighterII - Reinforcement Learning',
        'thumbnail': 'images/thumbnails/streetfighterII.gif',
        'description': 'Training a reinforcement learning agent to play StreetFighterII',
        'link': '/post/streetfighterII-RL.html'
    },

    {
        'title': 'Old School Runescape Grand Exchange - Time Series Prediction',
        'thumbnail': 'images/thumbnails/OSRS_GE.gif',
        'description': 'Training an LSTM to predict Grand Exchange prices.',
        'link': '/post/osrs_ge-lstm.html'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('front.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<link>')
def post(link):
    return render_template('/post/' + link)



