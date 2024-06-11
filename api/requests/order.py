select_purchase_order = """SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
            'id_order', purchase.id_order, 'order_date', purchase.order_date, 'status_order', purchase.status_order, 'total_value', purchase.total_value, 'payment_method', purchase.payment_method, 'portions_value', purchase.portions_value, 'often', purchase.often, 'delivery_infos', JSON_OBJECT(
                'street', purchase.delivery_street, 'cep', purchase.delivery_cep, 'state', purchase.delivery_state, 'number', purchase.delivery_number, 'complement', purchase.delivery_complement, 'city', purchase.delivery_city, 'receiver_name', purchase.delivery_receiver
            ), 'items', (
                Select JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'id_order_item', order_item.id_order_item, 'store_name', seller.store_name, 'id_product', order_item.id_product, 'quantity', order_item.quantity, 'warranty', product.warranty, 'price', order_item.price, 'name', product.name, 'category', category.name, 'brand', JSON_OBJECT(
                                'name', brand.name, 'logo', brand.brand_logo, 'logo_black', brand.brand_logo_black
                            ), 'images', (
                                Select JSON_ARRAYAGG(
                                        JSON_OBJECT(
                                            'path', image.path, 'index', image.index_image
                                        )
                                    )
                                from image
                                WHERE
                                    image.id_product = product.id
                            ), 'rating', JSON_OBJECT(
                                'amount_rating', rating.amount, 'rating_value', rating.rating, 'comments', (
                                    select JSON_ARRAYAGG(
                                            JSON_OBJECT(
                                                'id_comment', comment.id_comment, 'title_text', comment.title_text, 'rating_value', comment.rating_value, 'text_comment', comment.comment_text, 'created_at', comment.created_at
                                            )
                                        )
                                    FROM comment
                                    where
                                        comment.id_product = product.id
                                )
                            )
                        )
                    )
                from
                    order_item
                    LEFT JOIN product ON order_item.id_product = product.id
                    LEFT JOIN brand on product.brand_id = brand.id
                    LEFT JOIN category on product.category_id = category.id
                    LEFT JOIN rating on product.id = rating.id_product
                    LEFT JOIN seller on product.seller_id = seller.id

                WHERE
                    order_item.id_order = purchase.id_order
            )
        )
    ) as purchases
FROM purchase_order as purchase
WHERE
    purchase.id_customer = %s
ORDER BY purchase.order_date DESC
"""

select_purchase_order_id = """
SELECT JSON_OBJECT(
        'id_order', purchase.id_order, 'order_date', purchase.order_date, 'status_order', purchase.status_order, 'total_value', purchase.total_value, 'ship_value', purchase.ship_value, 'discount_value', purchase.discount_value, 'payment_method', purchase.payment_method, 'portions_value', purchase.portions_value, 'often', purchase.often, 'delivery_infos', JSON_OBJECT(
            'street', purchase.delivery_street, 'cep', purchase.delivery_cep, 'state', purchase.delivery_state, 'number', purchase.delivery_number, 'complement', purchase.delivery_complement, 'city', purchase.delivery_city, 'receiver_name', purchase.delivery_receiver 
        ), 'items', (
            Select JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'id_order_item', order_item.id_order_item, 'store_name', seller.store_name, 'id_product', order_item.id_product, 'quantity', order_item.quantity, 'warranty', product.warranty, 'price', order_item.price, 'name', product.name, 'category', category.name, 'brand', JSON_OBJECT(
                            'name', brand.name, 'logo', brand.brand_logo, 'logo_black', brand.brand_logo_black
                        ), 'images', (
                            Select JSON_ARRAYAGG(
                                    JSON_OBJECT(
                                        'path', image.path, 'index', image.index_image
                                    )
                                )
                            from image
                            WHERE
                                image.id_product = product.id
                        ), 'rating', JSON_OBJECT(
                            'amount_rating', rating.amount, 'rating_value', rating.rating, 'comments', (
                                select JSON_ARRAYAGG(
                                        JSON_OBJECT(
                                            'id_comment', comment.id_comment, 'title_text', comment.title_text, 'rating_value', comment.rating_value, 'text_comment', comment.comment_text, 'created_at', comment.created_at
                                        )
                                    )
                                FROM comment
                                where
                                    comment.id_product = product.id
                            )
                        )
                    )
                )
            from
                order_item
                LEFT JOIN product ON order_item.id_product = product.id
                LEFT JOIN brand on product.brand_id = brand.id
                LEFT JOIN category on product.category_id = category.id
                LEFT JOIN rating on product.id = rating.id_product
                LEFT JOIN seller on product.seller_id = seller.id
            WHERE
                order_item.id_order = purchase.id_order
        )
    ) as purchases
FROM purchase_order as purchase
WHERE
    purchase.id_order = %s"""

select_data_order = """
SELECT JSON_OBJECT(
        'discount', cart.discount, 'discount_value', cart.discount_value, 'product_total_value', cart.product_total_value, 'cart_total_value', cart.cart_total_value, 'voucher', cart.voucher, 'portions', cart.portions, 'ship_value', cart.ship_value, 'ship_deadline', cart.ship_deadline, 
        'items', JSON_ARRAYAGG(
            JSON_OBJECT(
                'id', items.id, 'product_id', items.id_product, 'amount', items.amount, 'name', p.name, 'value', JSON_OBJECT(
                    'price_now', vp.price_now, 'common_price', vp.common_price, 'portions', vp.portions, 'fees_monthly', vp.fees_monthly, 'fees_credit', vp.fees_credit
                )
            )
        ), 'ship', (
            SELECT JSON_OBJECT(
                    'district', district, 'city', cidade, 'state', estado, 'receiver_name', ship_info.receiver, 'street', street, 'cep', cep, 'complement', complement, 'ship_number', number, 'phone_number', phone_number
                )
            FROM ship_info
            WHERE
                id = cart.ship_id
        )
    ) AS cart
FROM
    cart_user cart
    LEFT JOIN cart_items items on cart.id_person = items.id_person
    LEFT JOIN value_product vp on items.id_product = vp.id_product
    LEFT JOIN product p on items.id_product = p.id
WHERE
    cart.id_person = %s
"""

insert_purchase_order = """
INSERT INTO
    purchase_order (
        id_order,
        id_customer,
        status_order,
        total_value,
        payment_method,
        portions_value,
        often,
        delivery_street,
        delivery_city,
        delivery_cep,
        delivery_state,
        delivery_number,
        delivery_complement,
        discount_value,
        ship_value,
        delivery_receiver
    )
VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
"""
