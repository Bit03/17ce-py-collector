# 基于17ce的监控项目手册

## 目录
- [项目说明](#项目说明)
- [文件结构](#文件结构)
- [部署方式](#部署方式)


## 项目说明

此项目主要是通过 python 的 APScheduler 框架，建立一个定时任务.
然后, 通过 17ce 的 websocket 的接口，拿到国内外相应节点访问链闻主页的测速数据.
然后. 将数据进行处理并写入相应的influxdb数据库中.


### 流程图如,图一所示,

[![image](https://user-images.githubusercontent.com/79570374/133237400-6e993a60-05fd-461e-8084-08cf714ae7bf.png)](https://user-images.githubusercontent.com/79570374/133237400-6e993a60-05fd-461e-8084-08cf714ae7bf.png)

### 写入数据库的字段有：省份、城市、运营商、总时间、下载时间、连接时间、解析时间和首字节时间，如图二所示。

[![image](https://user-images.githubusercontent.com/79570374/133237482-298a58b6-1607-41dd-b8bf-f5491550381f.png)](https://user-images.githubusercontent.com/79570374/133237482-298a58b6-1607-41dd-b8bf-f5491550381f.png)


## 文件结构

- main/
  - main.py # 项目的入口文件，用于配置logging和注册定时任务
  - settings.py # 项目配置文件
- jobs/
  - Job_17ce.py # 定时任务，通过utils目录中的文件，执行17ce的测速数据请求、处理以及写入数据库。
- utils/
  - data.py # 用于处理websocket请求数据、websocket返回数据以及将返回数据写入influxdb数据库
  - ws.py # 用于生成websocket所需的url和ssl

## 部署方式

* 环境变量：
  - 17CE_USER：17ce的账户
  - 17CE_API_PWD：17ce的api_pwd
  - LOG_LEVEL：logging的通知级别（默认为info）
  - 17CE_URL：测试的url（默认为"[https://www.chainnews.com](https://www.chainnews.com)"）
  - INFLUXDB_HOST
  - INFLUXDB_POST
  - INFLUXDB_USER
  - INFLUXDB_PWD
  - INFLUXDB_NAME


* docker running 

```
docker build -t 17ce-py-collector .

docker run 17ce-py-collector python main/main.py

```
