select_complete_cart = """
SELECT JSON_OBJECT(
        'discount', cart.discount, 'discount_value', cart.discount_value, 'product_total_value', cart.product_total_value, 'cart_total_value', cart.cart_total_value, 'voucher', cart.voucher, 'portions', cart.portions, 'ship_value', cart.ship_value, 'ship_street', cart.ship_street, 'ship_deadline', cart.ship_deadline, 'ship_cep', cart.ship_cep,
          'items', JSON_ARRAYAGG(
            JSON_OBJECT(
                'id', items.id, 'product_id', items.id_product, 'amount', items.amount, 'name', p.name, 'value', JSON_OBJECT(
                    'price_now', vp.price_now, 'common_price', vp.common_price, 'portions', vp.portions, 'fees_monthly', vp.fees_monthly, 'fees_credit', vp.fees_credit
                ), 'brand', b.name, 'images', (
                    SELECT JSON_ARRAYAGG(i.path)
                    FROM image i
                    WHERE
                        i.id_product = items.id_product
                )
            )
        )
    ) AS cart
FROM
    cart_user cart
    LEFT JOIN cart_items items on cart.id_person = items.id_person
    LEFT JOIN value_product vp on items.id_product = vp.id_product
    LEFT JOIN product p on items.id_product = p.id
    LEFT JOIN brand b on p.brand_id = b.id
WHERE
    cart.id_person = %s
"""
