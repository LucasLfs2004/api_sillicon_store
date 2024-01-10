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
                  SELECT
                    JSON_OBJECT(
                        'id',
                        person.id,
                        'name',
                        person.name,
                        'email',
                        person.email,
                        'birthday',
                        person.birthday,
                        'phone_number',
                        person.phone_number,
                        'cpf',
                        person.cpf,
                        'is_admin',
                        seller.admin,
                        'seller',
                        seller.seller,
                        'id_seller',
                        seller.id,
                        'cart',
                        CASE
                            WHEN COUNT(cart_user.id_person) > 0 THEN JSON_ARRAY(
                                JSON_OBJECT(
                                    'id',
                                    cart_user.id,
                                    'product_id',
                                    cart_user.id_product,
                                    'amount',
                                    cart_user.amount
                                )
                            )
                            ELSE JSON_ARRAY()
                        END
                    ) AS person
                FROM person
                    LEFT JOIN seller ON person.id = seller.id_person
                    LEFT JOIN cart_user on person.id = cart_user.id_person
                WHERE person.id = %s  
                GROUP BY
                    person.id,
                    seller.admin,
                    seller.seller,
                    seller.id,
                    cart_user.id,
                    cart_user.id_product,
                    cart_user.amount
                  """
