import db


add_user_cmd = """ INSERT INTO `studentTix`.`user` (`first_name`, `last_name`, `email`, `password`) VALUES (%s, %s, %s, %s);
"""

def add_user(first_name,last_name,email,password):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(add_user_cmd, [first_name, last_name, email, password])
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

add_ticket_cmd = """ INSERT INTO `studentTix`.`tickets` (`user_id`, `name`, `event`, `date_time`, `price`, `description`) VALUES (%s, %s, %s, %s, %s, %s); """

def add_ticket(user_id, name, event, time, price, description):
    conn = db.conn()
    cursor = conn.cursor()

    cursor.execute(add_ticket_cmd, [user_id, name, event, time, price, description])
    
