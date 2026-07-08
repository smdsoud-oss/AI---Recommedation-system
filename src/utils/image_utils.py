from PIL import Image
import os


def load_product_image(image_folder, image_name):
    """
    Load a product image.
    """

    image_path = os.path.join(
        image_folder,
        image_name
    )

    return Image.open(image_path)