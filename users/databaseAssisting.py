import sqlite3
from sqlite3 import Error


database = r"C:\\Users\matan\PycharmProjects\projectUI\psite\db.sqlite3"  # the location


def create_connection(db_file):
    """
    create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def is_activated(username):
    """
    Query tasks by priority
    :param username: the username to be searched
    :param priority:
    :return: activation
    """
    conn = create_connection(database)
    activation_query = ""
    cur = conn.cursor()
    id_query = "SELECT id FROM auth_user WHERE username='" + str(username) + "'"
    cur.execute(id_query)
    id = cur.fetchall()
    if id:
        id = id[0][0]
    try:
        activation_query = "SELECT activation FROM users_services WHERE user_id=" + str(id)
    except:
        print("error")
    cur.execute(activation_query)
    activations = cur.fetchall()
    for activation in activations:
        if activation[0] == 1:
            print("activate")
            return "1"
        else:
            print("not activate")
            return "0"


def get_message(username):
    """
    Query tasks by priority
    :param username: the usenrane to be searched
    :return: the message
    """
    conn = create_connection(database)

    cur = conn.cursor()
    id_query = "SELECT id FROM auth_user WHERE username='" + str(username) + "'"
    cur.execute(id_query)
    id = cur.fetchall()[0][0]
    activation_query = "SELECT message FROM users_comment WHERE user_id=" + str(id)
    cur.execute(activation_query)
    activations = cur.fetchall()
    for activation in activations:
        return str(activation[0])




