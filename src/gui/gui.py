import tkinter as tk
from tkinter import ttk

from src.database.database import Database
from src.requester.requester import Requester


class GUI(object):

    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("CBooks Exporter")
        self.set_elements()
        self.set_layout()
        self.parent.mainloop()

    def set_elements(self):
        # Tabs as navigation
        tab_parent = ttk.Notebook(self.parent)

        categories_tab = ttk.Frame(tab_parent)
        inventory_tab = ttk.Frame(tab_parent)
        orders_tab = ttk.Frame(tab_parent)
        settings_tab = ttk.Frame(tab_parent)

        tab_parent.add(categories_tab, text="Categories")
        tab_parent.add(inventory_tab, text="Inventory")
        tab_parent.add(orders_tab, text="Orders")
        tab_parent.add(settings_tab, text="Settings")

        tab_parent.pack(expand=1, fill="both")

        # Widgets for categories_tab
        categories_tree = ttk.Treeview(categories_tab, column=("c1", "c2", "c3", "c4"), show='headings')

        categories_tree.heading("#1", text="topCategory")
        categories_tree.column("#1", anchor=tk.CENTER)

        categories_tree.heading("#2", text="subCategory")
        categories_tree.column("#2", anchor=tk.CENTER)

        categories_tree.heading("#3", text="categoryNumber")
        categories_tree.column("#3", anchor=tk.CENTER)

        categories_tree.heading("#4", text="categoryID")
        categories_tree.column("#4", anchor=tk.CENTER)

        rows = Database().view_table("categories")

        for row in rows:
            # print(row)
            categories_tree.insert("", tk.END, values=row)

        categories_tree.pack()

        # Widgets for inventory_tab
        inventory_tree = ttk.Treeview(inventory_tab, column="c1", show='headings')

        inventory_tree.column("#1", anchor=tk.CENTER)
        inventory_tree.heading("#1", text="Category Number")

        inventory_tree.pack()

        # TODO Creation of the columns and implementation of the data import

        # Widgets for orders_tab
        # TODO Implementation of a TreeView that shows the orders

        # Widgets for settings_tab
        apikey_label = tk.Label(settings_tab, text="API key")
        apikey_label.pack()

        apikey = tk.Entry(settings_tab)
        apikey["show"] = "*"
        apikey.pack()

        # TODO Show the result of the authentication attempt
        submit = tk.Button(settings_tab, text="Test auth", command=lambda: Requester(apikey.get()))
        submit.pack()

        # api_requests.authenticate(apikey.get())

    def set_layout(self):
        # TODO implement variable full screen mode
        self.parent.geometry("1920x1080")

        # TODO The GUI is jerky for unknown reasons
        # Setting Theme
        # style = ThemedStyle(self.parent)
        # if settings.get_theme():
        #    style.set_theme("equilux")
        # else:
        #    style.set_theme("yaru")
