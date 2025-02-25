""" module to run server """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """ Home page """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_request():
    """ Function to calculate dominant emotion and return it back """
    statement = request.args.get('textToAnalyze')
    emotions = emotion_detector(statement)
    if emotions["dominant_emotion"] is None:
        return 'Invalid text! Please try again!'
    return f'For the given statement, the system response is {emotions}. \
                The dominant emotion is {emotions["dominant_emotion"]}.'
