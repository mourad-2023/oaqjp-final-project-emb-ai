from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_request():
    statement = request.args.get('textToAnalyze')
    emotions = emotion_detector(statement)
    if emotions["dominant_emotion"] == None:
        return 'Invalid text! Please try again!'
    return f'For the given statement, the system response is {emotions}. The dominant emotion is {emotions["dominant_emotion"]}.'
