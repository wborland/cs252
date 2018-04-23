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

get_user_groups = """SELECT to_id, from_id FROM `studentTix`.`messages` WHERE to_id = %s OR from_id = %s """
get_to_messages_in_group = """SELECT * FROM `studentTix`.`messages` WHERE to_id = %s AND from_id = %s"""
get_from_messages_in_group = """SELECT * FROM `studentTix`.`messages` WHERE to_id = %s AND from_id = %s"""


def get_all_user_messages(user_id):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(get_user_groups, [user_id, user_id])
    out = cursor.fetchall()
    group_set = set()
    return_dict = {}

    for pair in out:
        if pair[0] is not user_id:
            group_set.add(pair[0])
        else:
            group_set.add(pair[1])



    print(group_set)

    for user in group_set:
        print(user, user_id)
        cursor.execute(get_to_messages_in_group, [user_id, user])
        to_messages = cursor.fetchall()
        cursor.execute(get_from_messages_in_group, [user, user_id])
        from_messages = cursor.fetchall()
        single_dict = to_messages + from_messages
        sorted_tuple = sorted(single_dict,key=lambda x: x[0])
        name = get_user_name(user)
        return_dict[name] = sorted_tuple

    return return_dict



add_message = """INSERT INTO `studentTix`.`messages` (`to_id`, `from_id`, `message`) VALUES (%s, %s, %s);"""

def add_message(to_id, from_id, message):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(add_message, [to_id, from_id, message])
    conn.commit()

    return 1

user_name_cmd = """SELECT first_name, last_name FROM studentTix.user WHERE id = %s"""

def get_user_name(id):
    conn = db.conn()
    cursor = conn.cursor()
    cursor.execute(user_name_cmd, [id])
    out = cursor.fetchall()
    name = out[0][0] + " " + out[0][1]
    return name
    
