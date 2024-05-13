CREATE TABLE
    IF NOT EXISTS types (
        id INTEGER PRIMARY KEY,
        name STRING UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

INSERT INTO
    types (name)
VALUES
    ("illust"),
    ("manga"),
    ("ugoira") ON CONFLICT (name) DO NOTHING;