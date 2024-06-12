def organize_images_from_products(product):
    images = []
    
    swapped = False
    length_arr = len(product['images'])
    if len(product['images']) > 1:
        for i in range(length_arr):
            for j in range(0, length_arr-i-1):
                if product['images'][j]['index'] is None:
                    product['images'][j]['index'] = 20
                if product['images'][j + 1]['index'] is None:
                    product['images'][j + 1]['index'] = 20
                if product['images'][j]['index'] > product['images'][j + 1]['index']:
                    swapped = True
                    product['images'][j], product['images'][j +
                                                            1] = product['images'][j + 1], product['images'][j]

            if not swapped:
                return

    if product['images'] is not None:
        for image in product['images']:
            images.append(image['path'])

    return images
