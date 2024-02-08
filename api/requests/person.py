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
                            'id', person.id, 'name', person.name, 'email', person.email, 'birthday', person.birthday, 'phone_number', person.phone_number, 'cpf', person.cpf, 'is_admin', seller.admin, 'seller', seller.seller, 'id_seller', seller.id,  'principal_ship', person.principal_ship_id, 'ship_info', JSON_ARRAYAGG(
                                JSON_OBJECT(
                                    'ship_name', ship_info.name, 'phone_number', ship_info.phone_number, 'district', ship_info.district, 'city', ship_info.cidade, 'state', ship_info.estado, 'ship_id', ship_info.id, 'street', ship_info.street, 'cep', ship_info.cep, 'complement', ship_info.complement, 'ship_number', ship_info.number, 'receiver_name', ship_info.receiver
                                )
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
