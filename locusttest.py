#-*- coding: UTF-8 -*-
from locust import HttpLocust, TaskSet, task
import json
import requests

class WebsiteTasks(TaskSet):
    def on_start(self):
        pass

    @task(1)
    def getDeviceDiagramStst(self):
        request_url = "/tsp/fms-monitor/locusPage/eventPointsListInfo?vin=LFNMVXNX0AAD70955&startTime=1537173035000&endTime=1537176635000"
        headers = {"token":"0237957faea04015aba19f7b18b1f13d"}

        try:
            response = self.client.get( url=request_url, headers=headers, timeout=60)
        except(UnboundLocalError):
            print("interface file")
        try:
            response_text = json.loads(response.text)["status"]
        except:
            print ("被中断")
        else:
            if response.status_code != 200 and response_text != "SUCCEED":
                print ("返回内容：%s"%(response.text))
                print ("返回异常,请求状态码：%s"%(response.status_code))
            elif response.status_code == 200 and response_text == "SUCCEED":
                print ("返回成功")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    #请求响应时间
    min_wait = 120000
    max_wait = 120000
    host = "http://116.62.223.17:8005/"