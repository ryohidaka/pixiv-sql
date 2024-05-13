CREATE TABLE
    IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        illust_id STRING,
        page INTEGER,
        is_multiple_page INTEGER,
        filename STRING UNIQUE,
        url STRING UNIQUE,
        is_square INTEGER created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (illust_id) REFERENCES bookmarked_illusts (id)
    );