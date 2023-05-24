import json
import csv

with open('clients.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open('clients.csv', 'w', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    csv_writer.writerow(['id', 'name', 'surname', 'age', 'email', 'city'])

    for item in data:
        csv_writer.writerow([item['id'], item['name'], item['surname'], item['age'], item['email'], item['city']])