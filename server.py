from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetection")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    dom_emotion = emotions['dominant_emotion']
    del emotions['dom_emotion']
    output = f"For the given state, the system response is"
    for e, score in emotions.items():
        output = output + f"'{e}': {score},"
    output = output + f"The dominant emotion is {dom_emotion}"
    return output

@app.route("/")
def render_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)