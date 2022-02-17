import requests  # 导入requests包
import json


def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    From_data = {'i': word, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb',
                 'salt': '15477056211258', 'sign': 'd9c7e2bb300d203288200fb5de52ba02', 'lts': '1600140487052',
                 'bv': '47a528e99369d93772afe4364166b2da', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
                 'action': 'FY_BY_CLICKBUTTION', 'typoResult': 'false'}
    # 请求表单数据
    response = requests.post(url, data=From_data)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    # 打印翻译后的数据
    # print(content['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    get_translate_date('中国')
