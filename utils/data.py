import json
import logging

from influxdb import InfluxDBClient

from settings import base


def get_send_data():
    data = {
        "txnid": 1,
        "nodetype": base.NODE_TYPE,
        "num": base.NODE_NUM,
        "Url": base.URL,
        "TestType": "HTTP",
        "TimeOut": 120,
        "Request": "GET",
        "NoCache": False,
        "type": 1,
        "isps": base.ISPS,
        "areas": base.AREAS,
        "pro_ids": base.PRO_IDS,
        "city_ids": base.CITY_IDS,
        "UserAgent": "Mozilla/5.0 (Windows NT 5.1; rv:19.0) Gecko/20100101 Firefox/19.0",
    }

    return json.dumps(data)


def process_data(data, current_time):
    with open(base.ISP_PATH, "r") as f:
        isps = json.load(f)
    with open(base.CITY_PATH, "r") as f:
        citys = json.load(f)
    isp = data.get("NodeInfo").get("isp")
    pro_id = data.get("NodeInfo").get("pro_id")
    city_id = data.get("NodeInfo").get("city_id")
    total_time = data.get("TotalTime")
    down_time = data.get("DownTime")
    connect_time = data.get("ConnectTime")
    parse_time = data.get("NsLookup")
    firstbyte_time = data.get("TTFBTime")

    data = {
        "measurement": "speed",
        "time": current_time,
        "tags": {
            "isp": isps.get(isp),
            "province": citys.get(pro_id).get("prov"),
            "city": citys.get(pro_id).get(city_id),
        },
        "fields": {
            "total_time": total_time,
            "down_time": down_time,
            "connect_time": connect_time,
            "parse_time": parse_time,
            "firstbyte_time": firstbyte_time,
        },
    }
    return data


def write_data_to_db(data):
    logging.info(f"{len(data)} data received in total")
    logging.info("Writing data to the database")

    client = InfluxDBClient(
        base.DB_HOST,
        base.DB_PORT,
        base.DB_USER,
        base.DB_PASSWORD,
        base.DB_NAME,
    )
    res = client.write_points(data)
    logging.info(f"{res}") if res else logging.error(f"{res}")
    logging.info("\n\n")
