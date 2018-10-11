#-*- coding: UTF-8 -*-
import requests
import json

from log import logging


class Function(object):


    def __init__(self):
        pass

    def function(self):


        request_url = "tsp/continental-gateway/continental-gateway/realTimeUploadData"
        request_params = {"Content-type": "application/json"}
        request_json=""
        try:
            with open("D:/locust/real_time_upload_data.json", "r") as f:
                request_json = json.load(f)
        except (IOError):
            logging.error("open json file fail!!!")

        try:
            response = self.client.post(url=request_url, headers=request_params, data=json.dumps(request_json))
        except(UnboundLocalError):
            logging.error("json fail")

        if response.status_code != 200:
            logging.warning("返回内容：%s"%(response.text))
            logging.warning("返回异常,请求状态码：%s"%(response.status_code))