#Mysql 测试
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()
cursor.execute("select * from sys_permission")
for r in cursor.fetchall():
    print(r)
conn.close()
