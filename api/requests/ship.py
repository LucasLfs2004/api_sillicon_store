get_ship_info_request = """
    SELECT JSON_OBJECT(
            'principal_ship', person.principal_ship_id, 'ship_info', JSON_ARRAYAGG(
                JSON_OBJECT(
                    'ship_name', ship_info.name, 'phone_number', ship_info.phone_number, 'district', ship_info.district, 'city', ship_info.cidade, 'state', ship_info.estado, 'ship_id', ship_info.id, 'street', ship_info.street, 'cep', ship_info.cep, 'complement', ship_info.complement, 'ship_number', ship_info.number, 'receiver_name', ship_info.receiver
                )
            )
        ) AS ship
    FROM
        person
        LEFT JOIN ship_info on person.id = ship_info.id_person
    WHERE
        person.id = %s
    GROUP BY
        person.id
        """
