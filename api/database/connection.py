import mysql.connector

mysql_host = "127.0.0.1://3306/db-sillicon-store"
mysql_user = "root"
mysql_password = "/aCF&vTd#Me2M1:2"
mysql_db = "SILLICON_STORE"

mysql_connection = mysql.connector.connect(
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)
