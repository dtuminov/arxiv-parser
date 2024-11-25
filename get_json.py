import xmltodict
import requests
import time
import json
import os
import logging


# This will convert xml to json
def get_json(xml_list):
    dict_list = []
    if not os.path.isdir('json_files'):
        os.mkdir('json_files')

    for idx, (category, item) in enumerate(xml_list):
        data_dict = xmltodict.parse(item)
        json_data = json.dumps(data_dict)

        # Create a subdirectory for each category
        category_dir = os.path.join('json_files', category.replace('.', '_'))
        if not os.path.isdir(category_dir):
            os.mkdir(category_dir)

        filename = f'arXiv_{category}_{idx}.json'
        file_path = os.path.join(category_dir, filename)
        with open(file_path, 'w') as json_file:
            json_file.write(json_data)

        dict_list.append(json_data)
    return dict_list
