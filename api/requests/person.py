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


get_user_profile = """
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
