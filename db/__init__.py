from flask import g

import MySQLdb as sql
from MySQLdb.cursors import DictCursor

import db.util


def make_conn():
    return sql.connect(host="studenttix.czubge8ebda6.us-east-1.rds.amazonaws.com", db="studentTix", passwd="9T2wX62T5!^%t8",user="gustavo")

    
def conn():
    if not hasattr(g, 'db_conn'):
        g.db_conn = make_conn()

    return g.db_conn
