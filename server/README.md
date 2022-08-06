# Server

Set up venv.

    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt

Create and initialize Sqlite database.

    ./venv/bin/python init_db.py

Start server:

    ./venv/bin/python main.py
