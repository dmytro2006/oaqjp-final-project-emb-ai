'''
This is a web app for emotion detection
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    '''
    Emotion detection endpoint
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if not result['dominant_emotion']:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is \
    'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, \
    'joy': {result['joy']} and 'sadness': {result['sadness']}. \
    The dominant emotion is {result['dominant_emotion']}"

@app.route("/")
def index():
    '''
    Index page endpoint
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
