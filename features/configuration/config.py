import configparser
from csv import writer, reader

def get_config():
    config = configparser.ConfigParser()
    config.read(r'features/configuration/properties.ini')
    return config


def create_json_value_file(location_id,lat,lng):
    with open(r'features/resources/json_values.csv', 'w') as f:
        csv_writer = writer(f)
        csv_writer.writerow([location_id, lat, lng])


def read_json_value_file():
    with open(r'features/resources/json_values.csv', 'r') as f:
        csv_reader = reader(f)
        csv_rows = []
        for row in csv_reader:
            csv_rows.append(row)
        return csv_rows[0]



