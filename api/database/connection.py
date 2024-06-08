import pymysql.cursors

mysql_host = "127.0.0.1"
mysql_user = "root"
mysql_password = "GallardoLP-570"
mysql_db = "SILLICON_STORE"

# mysql_connection = mysql.connector.connect(
#     user=mysql_user,
#     password=mysql_password,
#     database=mysql_db
# )

mysql_connection = pymysql.connect(host=mysql_host,
                                   user=mysql_user,
                                   password=mysql_password,
                                   database=mysql_db,
                                   cursorclass=pymysql.cursors.DictCursor)
