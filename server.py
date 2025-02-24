from flask import Flask, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_request():
    statement = requests.args.get('textToAnalyze')
    return emotion_detector(statement)
