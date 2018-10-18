from pymongo import MongoClient

import json
import glob

options = {
    'url': 'mongodb://localhost:27017',
    'database': 'radio',
    'collection': 'slay'
}


def get_files():
    files = glob.glob('./data/*.json')
    data = []
    for file in files:
        fd = open(file, 'r')
        json_data = json.load(fd)
        data.append(json_data)

    return data


def main():
    client = MongoClient(options['url'])

    db = client[options['database']]

    db.drop_collection(options['collection'])

    collection = db[options['collection']]

    data = get_files()

    collection.insert_many(data)


if __name__ == '__main__':
    main()
