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
                description_product.description_html
            LIMIT %s;
                """

get_product_id = """
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
                WHERE product.id = %s
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

search_product_name = """
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
                        rating.rating
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
                WHERE product.name LIKE %s OR product.model LIKE %s
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
                rating.rating;
                """
