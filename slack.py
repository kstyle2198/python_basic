# 파이썬에서 슬랙으로 텍스트 메시지 보내기 입니다.
import requests
import json


class Slack_Msg():
    def __init__(self, msg):
        self.msg = msg
        self.sendmsg()

    def sendmsg(self):

        web_hook_url = 'https://hooks.slack.com/services/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'
        sendmsg = self.msg
        slack_msg = {'text': sendmsg}
        requests.post(web_hook_url, data=json.dumps(slack_msg))


if __name__ == "__main__":
    Slack_Msg("테스트 입니다.")
