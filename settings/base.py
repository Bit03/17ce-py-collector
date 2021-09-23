import os

# 存放ISP的json文件的path
ISP_PATH = f"{os.getcwd()}/settings/isp.json"
# 存放省、市的json文件的path
CITY_PATH = f"{os.getcwd()}/settings/city.json"

##### 17ce账户
USER = os.getenv("17CE_USER", default="jiaxin@bit03.com")
API_PWD = os.getenv("17CE_API_PWD", default="5IELKINMGJO5FNFD")

LOG_LEVEL = int(os.getenv("LOG_LEVEL", default=20))
##### 测试api相关变量
# 每个区域下分配节点数
NODE_NUM = 1
# 测速url
URL = os.getenv("17CE_URL", default="https://www.chainnews.com")
# 客户端类型 1.IDC 2.路由器 3.桌面客户端 4.手机wifi 5.手机4g
NODE_TYPE = [1, 2, 3, 4, 5]
# 指定需要测试的运营商，具体数值请参考isp.json
ISPS = [1, 2, 7]
# 测速区域 1.大陆 2.港澳台 3.国外
AREAS = [1, 2, 3]
# 指定需要测试的省市，具体数值请参考city.json
PRO_IDS = [
    12,
    49,
    79,
    80,
    180,
    183,
    184,
    188,
    189,
    190,
    192,
    193,
    194,
    195,
    196,
    221,
    227,
    235,
    236,
    238,
    239,
    241,
    243,
    250,
    346,
    349,
    350,
    351,
    352,
    353,
    354,
    355,
    356,
    357,
]
CITY_IDS = [
    12,
    246,
    471,
    602,
    202,
    424,
    1547,
    392,
    575,
    212,
    584,
    667,
    601,
    217,
    271,
    280,
    560,
    259,
    609,
    1018,
    275,
    277,
    279,
    293,
    719,
    582,
    461,
    587,
    532,
    539,
    557,
    573,
    574,
    590,
]

##### influxdb
DB_HOST = os.getenv("INFLUXDB_HOST", default="127.0.0.1")
DB_PORT = os.getenv("INFLUXDB_PORT", default=8086)
DB_USER = os.getenv("INFLUXDB_USER", default="")
DB_PASSWORD = os.getenv("INFLUXDB_PWD", default="")
DB_NAME = os.getenv("INFLUXDB_NAME", default="chainnews_connect")
