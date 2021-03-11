from PIL import Image as Img
import numpy as np


def lightning_detecter(image, loc, debug=False):

    img = Img.open(image)
    height, width = img.size

    cropped_img = img.crop(loc)
    cropped_img.show()

    RGB_matrix = np.array(cropped_img)

    if debug:
        for ij in np.ndindex(RGB_matrix.shape[:2]):
            print(ij, "\t -> \t", RGB_matrix[ij])

        print('Shape:\t', RGB_matrix.shape)
        print('\n')

    detected_lightning = False
    for ij in np.ndindex(RGB_matrix.shape[:2]):

        if (RGB_matrix[ij][0], RGB_matrix[ij][1], RGB_matrix[ij][2]) == (255, 255, 0):
            detected_lightning = True
            break

        if (RGB_matrix[ij][0], RGB_matrix[ij][1], RGB_matrix[ij][2]) == (255, 85, 0):
            detected_lightning = True
            break

        if (RGB_matrix[ij][0], RGB_matrix[ij][1], RGB_matrix[ij][2]) == (255, 255, 255):
            detected_lightning = True
            break

        if (RGB_matrix[ij][0], RGB_matrix[ij][1], RGB_matrix[ij][2]) == (255, 170, 0):
            detected_lightning = True
            break

        if (RGB_matrix[ij][0], RGB_matrix[ij][1], RGB_matrix[ij][2]) == (191, 0, 0):
            detected_lightning = True
            break

        if (RGB_matrix[ij][0], RGB_matrix[ij][1], RGB_matrix[ij][2]) == (255, 0, 0):
            detected_lightning = True
            break

    if debug:
        print('Lightning detected:', detected_lightning)

    return detected_lightning

trst_loc = (150, 740, 185, 770)
lightning_detecter("lightning3.png", trst_loc)

