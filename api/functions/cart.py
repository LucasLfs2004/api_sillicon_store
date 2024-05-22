from api.database.connection import mysql_connection
import json


async def calc_list_portions(array_cart: dict, id_person: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM portion WHERE id_cart_user = %s", (id_person,))
        mysql_connection.commit()
        for i in range(array_cart['portions']):
            total_value_items = 0
            for item in array_cart['items']:
                value_item = item['value']['price_now'] if item['value']['price_now'] is not None else item['value']['common_price']
                value_item *= item['amount']
                value_item *= (1 + item['value']['fees_credit'] / 100)
                if i > 0:
                    value_item *= (1 + item['value']
                                   ['fees_monthly'] / 100) ** (i + 1)
                total_value_items += value_item
            often = i + 1
            value_credit = round(
                (total_value_items + array_cart['ship_value']), 2)

            if array_cart['discount'] != 0 and array_cart['discount'] is not None:
                if array_cart['discount'] > 1:
                    value_credit = value_credit - array_cart['discount']
                else:
                    value_credit = value_credit - \
                        (value_credit * array_cart['discount'])

            value_portion = round(value_credit / (i + 1), 2)
            cursor.execute("INSERT INTO portion (id_cart_user, often, value_credit, value_portion) VALUES (%s, %s, %s, %s)",
                           (id_person, often, value_credit, value_portion))
            mysql_connection.commit()

            cursor.execute('''SELECT JSON_ARRAYAGG(
                                    JSON_OBJECT(
                                        'often', portion.often, 'value_credit', portion.value_credit, 'value_portion', portion.value_portion
                                    )
                                ) AS portions
                            from portion
                            where
                                id_cart_user = %s''', (id_person,))
            portions = cursor.fetchone()
        return json.loads(portions['portions'])
    except Exception as e:
        print(e)


async def organize_response_cart(cart: dict, id_person: str):
    array_cart = json.loads(cart["cart"])

    for item in array_cart['items']:
        item['images'] = sorted(item['images'])

    # Se precisar ordenar a lista de itens pelo nome do produto:
    array_cart['items'] = sorted(
        array_cart['items'], key=lambda x: x['name'])

    array_cart['list_portions'] = await calc_list_portions(array_cart=array_cart, id_person=id_person)

    return array_cart
