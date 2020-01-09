import csv

def get_table_from_file(file_name):
    table = []
    with open(file_name, "r") as file:
        lines = csv.reader(file, delimiter=',', quotechar='"')
        for row in lines:
            table.append(row)
    return table


def write_table_to_file(file_name, to_write):
    with open(file_name, "a") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(to_write)
