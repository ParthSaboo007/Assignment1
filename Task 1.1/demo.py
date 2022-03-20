from PIL import Image
import time
from utils import get_poly_image, get_json_data, get_bb_image


def main(img_path, json_path, alpha=0.5):
    ts = time.time()
    car_data = get_json_data(json_path)
    img = Image.open(img_path).convert('RGBA')
    poly_img = get_poly_image(car_data, img, alpha)
    poly_img.save(f"transparent_polygons/poly_{ts}_image.png")
    bb_img = get_bb_image(car_data, poly_img)
    #bb_img.save(f"bb_{ts}_image.png")
    bb_img.save(f"bounding boxes/bb_{ts}_image.png")
    return poly_img, bb_img


if __name__ == "__main__":
    img_path = input("Enter Image Path ")
    json_path = input("Enter Json Path ")
    main(img_path, json_path)
