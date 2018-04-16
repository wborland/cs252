
import db






add_user_cmd = """ INSERT INTO `studentTix`.`user` (`first_name`, `last_name`, `email`, `password`) VALUES (%s, %s, %s, %s);
"""

def add_user(first_name, last_name,email,password):
    conn = db.conn()
    cursor = conn.cursor()

    try:
        cursor.execute(add_user_cmd, [first_name, last_name, email, password])
        conn.commit()
        out = cursor.fetchone()

        return 1

    
