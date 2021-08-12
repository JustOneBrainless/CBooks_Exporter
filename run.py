from src.database.database import Database
from src.gui.gui import GUI


def start():
    Database()
    GUI()


if __name__ == '__main__':
    start()
