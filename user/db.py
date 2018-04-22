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

get_user_groups = """SELECT to_id, from_id FROM `studentTix`.`messages` WHERE to_id = 1 OR from_id = 1 """
get_to_messages_in_group = """SELECT date_time, message FROM `studentTix`.`messages` WHERE to_id = 1 AND from_id = %s"""

def get_all_user_messages(user):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(get_user_groups)
    out = cursor.fetchall()
    group_set = set()

    for pair in out:
        if pair[0] is not user:
            group_set.add(pair[0])
        else:
            group_set.add(pair[1])

    cursor.execute(get_to_messages_in_group, [2])
    to_messages = cursor.fetchall()
    print(to_messages)

    return out



add_message = """INSERT INTO `studentTix`.`messages` (`to_id`, `from_id`, `message`) VALUES (%s, %s, %s);"""

def add_message(to_id, from_id, message):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(add_message, [to_id, from_id, message])
    conn.commit()

    return 1
    
