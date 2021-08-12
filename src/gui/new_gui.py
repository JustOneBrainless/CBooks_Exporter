import tkinter as tk
from types import SimpleNamespace
from queue import Queue
from enum import Enum
from threading import Thread


class Messages(Enum):
    CLICK = 0


def updatecycle(guiref, model, queue):
    while True:
        msg = queue.get()
        if msg == Messages.CLICK:
            model.count += 1
            guiref.label.set("Clicked: {}".format(model.count))


def gui(root, queue):
    label = tk.StringVar()
    label.set("Clicked: 0")
    tk.Label(root, textvariable=label).pack()
    tk.Button(root, text="Click me!", command=lambda: queue.put(Messages.CLICK)).pack()
    return SimpleNamespace(label=label)


if __name__ == '__main__':
    root = tk.Tk()
    queue = Queue()
    guiref = gui(root, queue)
    model = SimpleNamespace(count=0)
    t = Thread(target=updatecycle, args=(guiref, model, queue,))
    t.daemon = True
    t.start()
    tk.mainloop()