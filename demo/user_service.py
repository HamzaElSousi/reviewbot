"""A small user-lookup service. Used to demo ReviewBot on a real PR.

This file intentionally contains several bugs so ReviewBot has something to
catch. Do not use any of this in production.
"""

import sqlite3


def get_user_email(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Build the query by interpolating the username straight into SQL.
    query = f"SELECT id, email FROM users WHERE name = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    # If no row matched, fetchone() returns None — this next line will crash.
    return user[1].lower()


def delete_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
    except Exception:
        pass


def deactivate_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
        conn.commit()
    except Exception:
        pass
