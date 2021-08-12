DB_URL = "data/database/CBooks.db"
CBOOKS_CATEGORY_PRESET = "data/cbooks_presets/categories.csv"

# Books are divided into categories, for example crime novels.
CATEGORIES = """
    CREATE TABLE IF NOT EXISTS categories (
    topCategory VARCHAR(255),
    subCategory VARCHAR(255),
    categoryNumber UNSIGNED INT NOT NULL,
    categoryID INTEGER PRIMARY KEY AUTOINCREMENT
    );"""

# Inventory for books.
BOOKS = """
CREATE TABLE IF NOT EXISTS books (
categoryNumber UNSIGNED INT,
author VARCHAR(255),
title TEXT NOT NULL,
publishingCompany VARCHAR(255),
edition UNSIGNED INT,
year UNSIGNED INT,
place VARCHAR(255),
cover VARCHAR(255),
status UNSIGNED INT NOT NULL,
description TEXT,
language VARCHAR(255),
isbn VARCHAR(255),
pages UNSIGNED INT,
format VARCHAR(255),
orderNo INTEGER PRIMARY KEY AUTOINCREMENT,
weightInGrams UNSIGNED INT,
price FLOAT NOT NULL,
coverURL TEXT,
keyword VARCHAR(255),
unlimitedPieces BOOLEAN,
newItem BOOLEAN,
firstEdition BOOLEAN,
signed BOOLEAN,
separateShippingCostsToGermany FLOAT,
categoryID INTEGER,
FOREIGN KEY (categoryID) REFERENCES categories (categoryID)
);"""