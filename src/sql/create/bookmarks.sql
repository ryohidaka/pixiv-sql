CREATE TABLE
    IF NOT EXISTS bookmarks (
        id INTEGER PRIMARY KEY,
        title STRING,
        type_id INTEGER,
        caption STRING,
        user_id INTEGER,
        create_date TIMESTAMP,
        visible INTEGER,
        illust_ai_type INTEGER,
        illust_book_style INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );