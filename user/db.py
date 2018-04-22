import db


add_user_cmd = """ INSERT INTO `studentTix`.`user` (`first_name`, `last_name`, `email`, `password`, `payment`) VALUES (%s, %s, %s, %s, %s);
"""

def add_user(first_name,last_name,email,password, payment):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(add_user_cmd, [first_name, last_name, email, password, payment])
    conn.commit()
    out = cursor.fetchone()

    return 1


login_user_cmd = """ SELECT * FROM `studentTix`.`user` WHERE email = %s """

def check_login(email, password):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(login_user_cmd, [email])
    out = cursor.fetchall()

    return 1

add_ticket_cmd = """INSERT INTO `studentTix`.`tickets` (`user_id`, `name`, `event`, `date_time`, `price`, `description`, `location`) VALUES (%s, %s, %s, %s, %s, %s, %s); """


def add_ticket(user_id, name, event, time, price, description, location):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(add_ticket_cmd, [user_id, name, event, time, price, description, location])
    conn.commit()
    print(cursor.fetchall())

    return 1

basic_search_cmd = """SELECT user_id, name, event, date_time, price, description, location FROM `studentTix`.`tickets`"""

def basic_search():
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(basic_search_cmd)
    out = cursor.fetchall()
    return out



def run_command(command):
    print(command)
    conn = db.conn()
    cursor = conn.cursor()
    cursor.execute(command)

    out = cursor.fetchall()
    return out
    
