#-*- coding: UTF-8 -*-
from locust import HttpLocust, TaskSet, task
import json
'''性能测试任务类'''
class WebsiteTasks(TaskSet):

#初始化函数
    def on_start(self):
        try:
            with open("D:/workspace/python/locusttest/interface/reportDataUpdate.json", "r") as f:
                self.request_json = json.load(f)
        except (IOError):
            print ("open interface json file fail!!!")

#任务
    @task(1)
    def get_tag_vals(self):
        u'''
        request_url:请求路径
        request_params:请求头参数
        request_json:请求json参数
        '''
        #logger = log.Logging.write_logging()
        request_url = "http://114.115.185.200:8005/tsp/continental-gateway/continental-gateway/reportDataUpdate"
        request_params = {"Content-type": "application/json"}
        request_json = self.request_json
        try:
            response = self.client.post(url=request_url, headers=request_params, data=json.dumps(request_json))
        except(UnboundLocalError):
            print ("json fail")

        if response.status_code != 200:
            print ("返回内容：%s"%(response.text))
            print ("返回异常,请求状态码：%s"%(response.status_code))
        elif response.status_code == 200:
            print ("返回成功")

#性能测试配置
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    #请求响应时间
    min_wait = 30
    max_wait = 40
    host = "http://114.115.185.200:8005/"
