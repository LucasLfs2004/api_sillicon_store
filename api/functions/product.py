def organize_images_from_products(product):
    images = []
    # print(product)
    # print(product['images'])

    swapped = False
    length_arr = len(product['images'])
    for i in range(length_arr):
        for j in range(0, length_arr-i-1):
            if product['images'][j]['index'] > product['images'][j + 1]['index']:
                swapped = True
                product['images'][j], product['images'][j +
                                                        1] = product['images'][j + 1], product['images'][j]

        if not swapped:
            return
    for image in product['images']:
        # print(image)
        images.append(image['path'])
    return images
