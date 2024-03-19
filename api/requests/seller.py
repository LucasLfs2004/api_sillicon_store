get_seller_data = """
select JSON_OBJECT(
        'store_name', s.store_name, 'id_seller', s.id, 'products_from_seller', (
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
            WHERE
                seller_id = s.id
            ORDER BY product.created_at
        )
    ) AS seller
FROM seller s
WHERE
    id_person = %s    """
