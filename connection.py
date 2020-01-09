import csv

def get_table_from_file(file_name):
    table = []
    with open(file_name, "r") as file:
        lines = csv.reader(file, delimiter=',', quotechar='"')
        for row in lines:
            table.append(row)
    return table


def write_table_to_file(file_name):
    with open(file_name, "a") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['1'] * 4 + ["test"])

if __name__ == '__main__':
    write_table_to_file("./static/question.csv")