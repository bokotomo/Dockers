# -*- coding: utf-8 -*-
import urllib.request
import json

class SlackSender:
    url=""
    channel=""
    username=""
    def __init__(self, url="", channel="", username=""):
        self.url=url
        self.channel=channel
        self.username=username

    def send(self, text):
        # スラックにメッセージを送る
        method = "POST"
        param = {
            "payload": {
                'channel': self.channel,
                'username': self.username,
                'text': text
            }
        }
        self.__send_http_request(url=self.url, method=method, param=param)

    def __send_http_request(self, url="", method="", param={}):
        # httpリクエストを送る
        response_body = ""
        encoded_param = urllib.parse.urlencode(param).encode(encoding='utf-8')
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(param).encode("utf-8")
        with urllib.request.urlopen(url=url, data=encoded_param) as response:
            response_body = response.read().decode("utf-8")

