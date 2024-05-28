get_persons_query = """
                   SELECT
                        person.id,
                        person.name,
                        person.cpf,
                        person.email,
                        person.birthday,
                        person.phone_number,
                        seller.admin as isAdmin,
                        seller.seller as isSeller,
                        seller.id as idSeller
                    FROM
                        person
                    LEFT JOIN
                        seller ON person.id = seller.id_person;
                   """


get_person_id_query = """SELECT
                        person.id,
                        person.password,
                        person.name,
                        person.email,
                        seller.admin as is_admin,
                        seller.seller as is_seller,
                        seller.id as id_seller
                    FROM
                        person
                    LEFT JOIN
                        seller ON person.id = seller.id_person
                    WHERE person.email = %s"""


get_user_profile_old = """
                    SELECT
                        person.id,
                        person.name,
                        person.email,
                        person.birthday,
                        person.phone_number,
                        person.cpf,
                        seller.admin as is_admin,
                        seller.seller as is_seller,
                        seller.id as id_seller
                    FROM
                        person
                        LEFT JOIN seller ON person.id = seller.id_person
                    WHERE
                        person.id = %s"""
get_user_profile = """
SELECT JSON_OBJECT(
        'id', person.id, 'name', person.name, 'email', person.email, 'birthday', person.birthday, 'phone_number', person.phone_number, 'cpf', person.cpf, 'is_admin', seller.admin, 'seller', seller.seller, 'id_seller', seller.id, 'principal_ship', person.principal_ship_id, 'ship_info', JSON_ARRAYAGG(
            JSON_OBJECT(
                'ship_name', ship_info.name, 'phone_number', ship_info.phone_number, 'district', ship_info.district, 'city', ship_info.cidade, 'state', ship_info.estado, 'ship_id', ship_info.id, 'street', ship_info.street, 'cep', ship_info.cep, 'complement', ship_info.complement, 'ship_number', ship_info.number, 'receiver_name', ship_info.receiver
            )
        ), 'last_order', (
            SELECT JSON_OBJECT(
                    'id_order', purchase.id_order, 'order_date', purchase.order_date, 'status_order', purchase.status_order, 'total_value', purchase.total_value, 'payment_method', purchase.payment_method, 'portions_value', purchase.portions_value, 'often', purchase.often, 'delivery_infos', JSON_OBJECT(
                        'street', purchase.delivery_street, 'cep', purchase.delivery_cep, 'state', purchase.delivery_state, 'number', purchase.delivery_number, 'complement', purchase.delivery_complement, 'city', purchase.delivery_city
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
            FROM purchase_order as purchase
            WHERE
                purchase.id_customer = person.id
            ORDER BY purchase.order_date DESC
            LIMIT 1
        )
    ) AS person
FROM
    person
    LEFT JOIN seller ON person.id = seller.id_person
    LEFT JOIN ship_info on person.id = ship_info.id_person
WHERE
    person.id = %s
GROUP BY
    person.id,
    seller.admin,
    seller.seller,
    seller.id
                  """
