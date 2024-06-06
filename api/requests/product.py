get_all_products = """
            SELECT
                JSON_OBJECT(
                    'id',
                    product.id,
                    'name',
                    product.name,
                    'stock',
                    product.stock,
                    'warranty',
                    product.warranty,
                    'model',
                    product.model,
                    'featured',
                    product.featured,
                    'active',
                    product.active,
                    'brand',
                    brand.name,
                    'category',
                    category.name,
                    'value',
                    JSON_OBJECT(
                        'price_now',
                        value_product.price_now,
                        'common_price',
                        value_product.common_price,
                        'portions',
                        value_product.portions,
                        'fees_monthly',
                        value_product.fees_monthly,
                        'fees_credit',
                        value_product.fees_credit
                    ),
                    'rating',
                    JSON_OBJECT(
                        'amount_rating',
                        rating.amount,
                        'rating_value',
                        rating.rating,
                        'comments',
                        CASE
                            WHEN COUNT(comment.id_comment) > 0 THEN JSON_ARRAY(
                                JSON_OBJECT(
                                    'id_comment',
                                    comment.id_comment,
                                    'rating_value',
                                    comment.rating_value,
                                    'title_text',
                                    comment.title_text,
                                    'text_comment',
                                    comment.comment_text
                                )
                            )
                            ELSE JSON_ARRAY()
                        END
                    ),
                    'description',
                    JSON_OBJECT(
                        'desc_html',
                        description_product.description_html,
                        'updated_at',
                        description_product.updated_at
                    ),
                    'images',
                    JSON_ARRAYAGG(image.path)
                ) AS product
            FROM product
                LEFT JOIN category ON product.category_id = category.id
                LEFT JOIN brand ON product.brand_id = brand.id
                LEFT JOIN value_product ON product.id = value_product.id_product
                LEFT JOIN rating ON product.id = rating.id_product
                LEFT JOIN image ON product.id = image.id_product
                LEFT JOIN comment ON product.id = comment.id_product
                LEFT JOIN description_product ON product.id = description_product.id_product
            GROUP BY
                product.id,
                product.name,
                product.stock,
                product.warranty,
                product.model,
                product.featured,
                product.active,
                brand.name,
                category.name,
                value_product.price_now,
                value_product.common_price,
                value_product.portions,
                value_product.fees_monthly,
                value_product.fees_credit,
                rating.amount,
                rating.rating,
                comment.id_comment,
                comment.rating_value,
                comment.title_text,
                comment.comment_text,
                description_product.updated_at,
                description_product.description_html;
                """

get_limit_products = """
            SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'id', product.id, 'name', product.name, 'stock', product.stock, 'warranty', product.warranty, 'model', product.model, 'featured', product.featured, 'active', product.active, 'category', category.name, 'brand', JSON_OBJECT(
                            'name', brand.name, 'logo', brand.brand_logo, 'logo_black', brand.brand_logo_black
                        ), 'images', (
                            Select JSON_ARRAYAGG(JSON_OBJECT('path', image.path, 'index', image.index_image))
                            from image
                            WHERE
                                image.id_product = product.id
                        ), 'value', JSON_OBJECT(
                            'price_now', value_product.price_now, 'common_price', value_product.common_price, 'portions', value_product.portions, 'fees_monthly', value_product.fees_monthly, 'fees_credit', value_product.fees_credit
                        ), 'rating', JSON_OBJECT(
                            'amount_rating', rating.amount, 'rating_value', rating.rating, 'comments', (select JSON_ARRAYAGG(JSON_OBJECT('id_comment', comment.id_comment, 'title_text', comment.title_text, 'rating_value', comment.rating_value, 'text_comment', comment.comment_text, 'created_at', comment.created_at)) FROM comment where comment.id_product = product.id)
                        ), 'description', JSON_OBJECT(
                            'desc_html', description_product.description_html, 'updated_at', description_product.updated_at
                        )
                    )
                ) as products
            FROM
                product
                LEFT JOIN category on product.category_id = category.id
                LEFT JOIN brand on product.brand_id = brand.id
                LEFT JOIN value_product on product.id = value_product.id_product
                LEFT JOIN rating on product.id = rating.id_product
                LEFT JOIN description_product on product.id = description_product.id_product
            ORDER BY product.created_at
            LIMIT %s"""


get_product_id = """
SELECT JSON_OBJECT(
        'id', product.id, 'name', product.name, 'stock', product.stock, 'warranty', product.warranty, 'model', product.model, 'featured', product.featured, 'active', product.active, 'category', category.name, 'brand', JSON_OBJECT(
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
        ), 'value', JSON_OBJECT(
            'price_now', value_product.price_now, 'common_price', value_product.common_price, 'portions', value_product.portions, 'fees_monthly', value_product.fees_monthly, 'fees_credit', value_product.fees_credit
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
        ), 'description', JSON_OBJECT(
            'desc_html', description_product.description_html, 'updated_at', description_product.updated_at
        )
    ) as product
FROM
    product
    LEFT JOIN category on product.category_id = category.id
    LEFT JOIN brand on product.brand_id = brand.id
    LEFT JOIN value_product on product.id = value_product.id_product
    LEFT JOIN rating on product.id = rating.id_product
    LEFT JOIN description_product on product.id = description_product.id_product
WHERE
    product.id = %s
            """

search_product_name = """
            SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
            'id', product.id, 'name', product.name, 'stock', product.stock, 'warranty', product.warranty, 'model', product.model, 'featured', product.featured, 'active', product.active, 'category', category.name, 'brand', JSON_OBJECT(
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
            ), 'value', JSON_OBJECT(
                'price_now', value_product.price_now, 'common_price', value_product.common_price, 'portions', value_product.portions, 'fees_monthly', value_product.fees_monthly, 'fees_credit', value_product.fees_credit
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
            ), 'description', JSON_OBJECT(
                'desc_html', description_product.description_html, 'updated_at', description_product.updated_at
            )
        )
    ) as products
FROM
    product
    LEFT JOIN category on product.category_id = category.id
    LEFT JOIN brand on product.brand_id = brand.id
    LEFT JOIN value_product on product.id = value_product.id_product
    LEFT JOIN rating on product.id = rating.id_product
    LEFT JOIN description_product on product.id = description_product.id_product
    WHERE product.name LIKE %s OR product.model LIKE %s
                """


get_limit_products_specific_brand = """
            SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'id', product.id, 'name', product.name, 'stock', product.stock, 'warranty', product.warranty, 'model', product.model, 'featured', product.featured, 'active', product.active, 'category', category.name, 'brand', JSON_OBJECT(
                            'name', brand.name, 'logo', brand.brand_logo, 'logo_black', brand.brand_logo_black
                        ), 'images', (
                            Select JSON_ARRAYAGG(JSON_OBJECT('path', image.path, 'index', image.index_image))
                            from image
                            WHERE
                                image.id_product = product.id
                        ), 'value', JSON_OBJECT(
                            'price_now', value_product.price_now, 'common_price', value_product.common_price, 'portions', value_product.portions, 'fees_monthly', value_product.fees_monthly, 'fees_credit', value_product.fees_credit
                        ), 'rating', JSON_OBJECT(
                            'amount_rating', rating.amount, 'rating_value', rating.rating, 'comments', (select JSON_ARRAYAGG(JSON_OBJECT('id_comment', comment.id_comment, 'title_text', comment.title_text, 'rating_value', comment.rating_value, 'text_comment', comment.comment_text, 'created_at', comment.created_at)) FROM comment where comment.id_product = product.id)
                        ), 'description', JSON_OBJECT(
                            'desc_html', description_product.description_html, 'updated_at', description_product.updated_at
                        )
                    )
                ) as products
            FROM
                product
                LEFT JOIN category on product.category_id = category.id
                LEFT JOIN brand on product.brand_id = brand.id
                LEFT JOIN value_product on product.id = value_product.id_product
                LEFT JOIN rating on product.id = rating.id_product
                LEFT JOIN description_product on product.id = description_product.id_product
            WHERE brand.id = %s
            ORDER BY product.created_at
            LIMIT %s
                """

get_limit_products_specific_category = """
            SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'id', product.id, 'name', product.name, 'stock', product.stock, 'warranty', product.warranty, 'model', product.model, 'featured', product.featured, 'active', product.active, 'category', category.name, 'brand', JSON_OBJECT(
                            'name', brand.name, 'logo', brand.brand_logo, 'logo_black', brand.brand_logo_black
                        ), 'images', (
                            Select JSON_ARRAYAGG(JSON_OBJECT('path', image.path, 'index', image.index_image))
                            from image
                            WHERE
                                image.id_product = product.id
                        ), 'value', JSON_OBJECT(
                            'price_now', value_product.price_now, 'common_price', value_product.common_price, 'portions', value_product.portions, 'fees_monthly', value_product.fees_monthly, 'fees_credit', value_product.fees_credit
                        ), 'rating', JSON_OBJECT(
                            'amount_rating', rating.amount, 'rating_value', rating.rating, 'comments', (select JSON_ARRAYAGG(JSON_OBJECT('id_comment', comment.id_comment, 'title_text', comment.title_text, 'rating_value', comment.rating_value, 'text_comment', comment.comment_text, 'created_at', comment.created_at)) FROM comment where comment.id_product = product.id)
                        ), 'description', JSON_OBJECT(
                            'desc_html', description_product.description_html, 'updated_at', description_product.updated_at
                        )
                    )
                ) as products
            FROM
                product
                LEFT JOIN category on product.category_id = category.id
                LEFT JOIN brand on product.brand_id = brand.id
                LEFT JOIN value_product on product.id = value_product.id_product
                LEFT JOIN rating on product.id = rating.id_product
                LEFT JOIN description_product on product.id = description_product.id_product
            WHERE category.id = %s
            ORDER BY product.created_at
            LIMIT %s
                """