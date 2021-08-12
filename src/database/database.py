import csv
import os
import sqlite3

from src.database.constants import *


class Database(object):

    def __init__(self, path=None, tables=None):
        if path is None:
            path = DB_URL
        if tables is None:
            tables = [CATEGORIES, BOOKS]

        self.path = path
        self.tables = tables

        self.create()

    def create(self):
        if os.path.isfile(self.path):
            return

        connection = sqlite3.connect(self.path)

        for table in self.tables:
            cursor = connection.cursor()
            cursor.execute(table)
            connection.commit()

        if self.tables == [CATEGORIES, BOOKS]:
            self.import_cbooks_categories()

    def view_table(self, table):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + table)

        content = cursor.fetchall()
        connection.close()
        return content

    # Imports divisions (book categories) from a CSV file.
    def import_cbooks_categories(self, file_path=None):
        if file_path is None:
            file_path = CBOOKS_CATEGORY_PRESET

        with open(file_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            connection = sqlite3.connect(self.path)
            cursor = connection.cursor()

            # Parse through each line
            for row in csv_reader:
                if line_count == 0:
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # Find sqlite3 operational errors triggered by csv`s content.
                    # print(f'Processed {line_count} lines.')

                    # Catch unwanted chars and replace them
                    for element in row[1]:
                        if element == "'":
                            row[1] = row[1].replace("'", "''")
                            # print(row[1])

                    # Define category execute command.
                    category = "INSERT INTO categories (topCategory,subCategory,categoryNumber) VALUES ('{}', " \
                               "'{}', {})".format(row[0], row[1], row[2])
                    # print(category)
                    cursor.execute(category)

                    line_count += 1

            connection.commit()
            connection.close()

        # print(f'Processed {line_count} lines.')
        # print("Import was successful!")
        return True
