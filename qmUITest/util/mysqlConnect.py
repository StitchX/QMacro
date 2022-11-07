import pymysql

# 打开数据库连接
connect = pymysql.connect(
    host='47.105.92.166',
    user = 'root',
    password='krly2021',
    database='db_game_platform_prd_v4'
)

# 创建一个游标对象
cursor = connect.cursor()

# 执行execute查询

cursor.execute("select acc_nickname from tbl_user where id=1")
data = cursor.fetchone()
print(data[0])