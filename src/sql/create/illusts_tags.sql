CREATE TABLE
    IF NOT EXISTS illusts_tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        illust_id INTEGER,
        tag_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (illust_id) REFERENCES bookmarked_illusts (id),
        FOREIGN KEY (tag_id) REFERENCES tags (id)
    );