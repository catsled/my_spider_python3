from scrapy.conf import settings
from pymongo import MongoClient
from redis import Redis
import json

try:
    m_client = MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
    m_db = m_client['weather_d']
    m_col = m_db['weather']
    redis_cli = Redis(settings['REDIS_HOST'], settings['REDIS_PORT'], settings['REDIS_DB'])
except Exception as e:
    print(e)


def save_data_into_mongo():
    """将数据从redis中存入mongo中"""
    while True:
        source, data = redis_cli.blpop('past_weather:items')
        str_data = data.decode()
        dict_data = json.loads(str_data)
        print('insert-----', dict_data)
        m_col.insert(dict_data)

if __name__ == '__main__':
    save_data_into_mongo()