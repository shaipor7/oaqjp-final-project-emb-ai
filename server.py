''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/emotionDetector")
def sent_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows emotion scores and dominant emotion
        score for the provided text.
    '''
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)
    if response["dominant_emotion"] is None:
        result = "Invalid text! Please try again!"
    else:
        result = f"""
            For the given statement, the system response is 
            'anger': {response["anger"]}, 'disgust': {response["disgust"]}, 
            'fear': {response["fear"]}, 'joy': {response["joy"]} and 'sadness': {response["sadness"]}. 
            The dominant emotion is {response["dominant_emotion"]}.
            """
    return result


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host ="0.0.0.0", port = 5000, debug =True)
