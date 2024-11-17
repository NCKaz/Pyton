# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as csv_f:
        # TODO считать содержимое csv файла
      csv_dict = [str_ for str_ in csv.DictReader(csv_f)]

    with open(OUTPUT_FILENAME, "w") as json_f:
        json.dump(csv_dict, json_f, indent= 4)
      # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
