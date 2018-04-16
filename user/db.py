
import db


create_user_cmd = """
    SELECT * FROM user
"""


def create_user():
    conn = db.conn()
    cursor = conn.cursor()
    cursor.execute(create_user_cmd)

    out = cursor.fetchall()
    print(out)
    return "out"


