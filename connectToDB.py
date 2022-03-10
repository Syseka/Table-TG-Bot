# connectToDB.py

import mysql.connector
from mysql.connector import Error
from configDB import usH, usN, usP
    # import modules and DB log:pass from file

table = """CREATE TABLE `a0263496_bfb_stat_tgbot`.`TableTest` (
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` VARCHAR(32) NOT NULL,
  `match` VARCHAR(32) NOT NULL,
  `tip` VARCHAR(50) NOT NULL,
  `odds` VARCHAR(50) NOT NULL,
  `score` VARCHAR(50) NOT NULL,
  `result` VARCHAR(50) NOT NULL,
  `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"""

addstr = """INSERT INTO `a0263496_bfb_stat_tgbot`.`TableTest` 
(`date`,`match`,`tip`,`odds`,`score`,`result`)
VALUES
('test1','test2','test3','test4','test5', 'test6')
"""

def connectDB(hostN, userN, userP):
    global connection
# its really need
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostN,
            user = userN,
            passwd = userP)
        #print('Ok.')
    except Error as e:
        print(f'Error: {e}')

    return connection

connectDB(usH, usN, usP)

def addValue(connection,value):
    connection
    cursor = connection.cursor()
    try:
        cursor.execute(value)
        connection.commit()
        #print("Добавил.")
    except Error as e:
        print(f"Error: {e}")

def creatDB_Table(connect, query):
# Funk to make table in MySQL
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        connect.commit()
        #print("Таблица создана.")
    except Error as e:
        print(f"Error: {e}")

# creatDB_Table(connection, table)

addValue(connection,addstr)