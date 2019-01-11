from flask import Flask
from flask import request
from redis import Redis
from scripts.slack_sender import SlackSender

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    val = request.args.get("msg", "Not defined")
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times!\n<br>{}'.format(count, val)

@app.route('/api/v1/send', methods=['POST'])
def send_slack():
  if request.form["text"] == "":
    return "false"
  text = request.form["text"]
  url = "https://hooks.slack.com/services/" 
  channel = ""
  username = ""
  ss = SlackSender(url=url, channel=channel, username=username)
  ss.send(text)
  return 'true'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

