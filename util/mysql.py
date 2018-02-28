import pymysql

conn = pymysql.connect(host="172.17.88.6", port=3386, user="zhops", passwd="zhops2018", db="zhops", charset="utf8")
cur = conn.cursor()


def select_table(table, column, condition, value):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines


def select_columns(table, column):
    sql = "select " + column + " from " + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines
