#coding:utf-8
# use cmd5 api to decode md5
# python script for alfred workflow
# author: LANVNAL

import requests
import re
import sys
# from alfred.feedback import Feedback
from workflow import Workflow3

def generate_feedback_results(judge_code,result):
    wf = Workflow3()
    if(judge_code == 1):
        kwargs = {
                    'title': result,
                    'subtitle': '' ,
                    "valid": True,
                    'arg': result
                }
    else:
        kwargs = {
                    'title': result,
                    'subtitle': '' ,
                    'valid': False
                }
    wf.add_item(**kwargs)
    wf.send_feedback()


def main():
    url2 = 'http://ip-api.com/json/'  # 外国网站
    args = sys.argv[1]
    if len(args.split('.')) != 4:
        generate_feedback_results(0, "IP格式不正确")
    else:
        url2 = url2 + format(args)
        response2 = requests.get(url2)
        strpp = response2.json()  # 把英文网站json接口返回值传给字典strpp
        # generate_feedback_results(1, "国家：{:s} 城市：{:s} 经纬度坐标：{:f},{:f} 运营商编号：{:s} ISP服务商：{:s}".format(
        #     strpp.get('country'), strpp.get('city'), strpp.get('lat'), strpp.get('lon'), strpp.get('as'), strpp.get('isp')
        # ))
        generate_feedback_results(1, "国家：{:s} 城市：{:s}".format(strpp.get('country'), strpp.get('city')))


if __name__ == "__main__":
    main()