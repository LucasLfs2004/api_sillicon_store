select_purchase_order = """SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
            'id_order', purchase.id_order, 'order_date', purchase.order_date, 'status_order', purchase.status_order, 'total_value', purchase.total_value, 'payment_method', purchase.payment_method, 'portions_value', purchase.portions_value, 'often', purchase.often, 'delivery_infos', JSON_OBJECT(
                'street', purchase.delivery_street, 'cep', purchase.delivery_cep, 'state', purchase.delivery_state, 'number', purchase.delivery_number, 'complement', purchase.delivery_complement, 'city', purchase.delivery_city
            ), 'items', (
                Select JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'id_order_item', order_item.id_order_item, 'id_product', order_item.id_product, 'quantity', order_item.quantity, 'warranty', product.warranty, 'price', order_item.price, 'name', product.name, 'category', category.name, 'brand', JSON_OBJECT(
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
                WHERE
                    order_item.id_order = purchase.id_order
            )
        )
    ) as purchases
FROM purchase_order as purchase
WHERE
    purchase.id_customer = %s"""

select_purchase_order_id = """
SELECT JSON_OBJECT(
        'id_order', purchase.id_order, 'order_date', purchase.order_date, 'status_order', purchase.status_order, 'total_value', purchase.total_value, 'payment_method', purchase.payment_method, 'portions_value', purchase.portions_value, 'often', purchase.often, 'delivery_infos', JSON_OBJECT(
            'street', purchase.delivery_street, 'cep', purchase.delivery_cep, 'state', purchase.delivery_state, 'number', purchase.delivery_number, 'complement', purchase.delivery_complement, 'city', purchase.delivery_city
        ), 'items', (
            Select JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'id_order_item', order_item.id_order_item, 'id_product', order_item.id_product, 'quantity', order_item.quantity, 'warranty', product.warranty, 'price', order_item.price, 'name', product.name, 'category', category.name, 'brand', JSON_OBJECT(
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
            WHERE
                order_item.id_order = purchase.id_order
        )
    ) as purchases
FROM purchase_order as purchase
WHERE
    purchase.id_order = %s"""
