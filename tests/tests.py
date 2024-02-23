import json
import time
import mysql.connector
from request import new_get_products_limit

mysql_host = "127.0.0.1://3306/sillicon_store"
mysql_user = "admin"
mysql_password = "admin"
mysql_db = "SILLICON_STORE"

mysql_connection = mysql.connector.connect(
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)


if __name__ == "__main__":
    cursor = mysql_connection.cursor(dictionary=True)

    cursor.execute(new_get_products_limit, (40,))
    data = cursor.fetchone()
    # print(data)
    data = json.loads(data['products'])

    for product in data:
        images = []
        # print(product)
        # print(product['images'])

        swapped = False
        length_arr = len(product['images'])
        for i in range(length_arr):
            for j in range(0, length_arr-i-1):
                if product['images'][j]['index'] > product['images'][j + 1]['index']:
                    swapped = True
                    product['images'][j], product['images'][j +
                                                            1] = product['images'][j + 1], product['images'][j]
        for image in product['images']:
            # print(image)
            images.append(image['path'])
        product['images'] = images
        # print(product)

    print(data)
