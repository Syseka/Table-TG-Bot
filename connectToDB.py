# connectToDB.py

import mysql.connector
from mysql.connector import Error
from configDB import usH, usN, usP

#table = """CREATE TABLE `a0263496_bfb_stat_tgbot`.`Table1` (
#  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
#  `date` VARCHAR(32) NOT NULL,
#  `tip` VARCHAR(500) NOT NULL,
#  `odds` VARCHAR(500) NOT NULL,
#  `score` ENUM('w','l','m') NOT NULL,
#  `result` ENUM('w','l','m') NOT NULL,
#  `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#  PRIMARY KEY (`id`)
#) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"""

def connectDB(hostN, userN, userP):
    global connection
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostN,
            user = userN,
            passwd = userP)
        print('Ok.')
    except Error as e:
        print(f'Error: {e}')

    return connection

connectDB(usH, usN, usP)

#def creatDB_Table(connect, query):
# Funk to make table in MySQL
#    cursor = connect.cursor()
#    try:
#        cursor.execute(query)
#        connect.commit()
#        print("Таблица создана.")
#    except Error as e:
#        print(f"Error: {e}")
# creatDB_Table(connection, table)