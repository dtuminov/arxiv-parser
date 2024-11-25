# pip install xmltodict
import xmltodict
import requests
import time
import json
import os
import logging

from get_url_list import get_url_list
import xml.etree.ElementTree as ET


# This will get all the urls and save a list of XML documents
def get_xml(url_list):
    xml_list = []
    for category, url in url_list:
        try:
            data = requests.get(url)
            print(data.text)
            xml_list.append((category, data.text))  # Сохраняем категорию с данными XML.
        except Exception as e:
            print(f"Ошибка при получении URL. {url}: {e}")
            continue
        print('Ждем 3 секунды...')
        time.sleep(3)
    return xml_list
