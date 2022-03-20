import json
import numpy as np
from PIL import Image
from PIL import ImageDraw


def get_original_coordinates(normalized_coordinates, width, height):
    original_coordinates = []
    for coordinate in normalized_coordinates:
        x = int(coordinate[0] * width / 100)
        y = int(coordinate[1] * height / 100)
        original_coordinates.append((x, y))
    return original_coordinates


def get_bounding_box_coordinates(original_coordinates):
    np_coords = np.array(original_coordinates)
    min_coords = np_coords.min(axis=0)
    max_coords = np_coords.max(axis=0)
    bounding_box_coords = [tuple(min_coords), tuple(max_coords)]
    return bounding_box_coords


def get_poly_image(car_data, img, alpha):
    for index, item in enumerate(car_data):

        if item["type"] == "polygonlabels":
            img_width = item["original_width"]
            img_height = item["original_height"]
            xy = get_original_coordinates(item["value"]["points"], img_width, img_height)
            img2 = img.copy()
            draw = ImageDraw.Draw(img2)
            fill_color = tuple(np.random.choice(range(256), size=3))
            outline_color = tuple(int(round(item * 2 / 4, 0)) for item in fill_color)
            item["value"]["outline_color"] = outline_color
            draw.polygon(xy, fill=fill_color, outline=outline_color)
            img = Image.blend(img, img2, alpha)
    return img


def get_bb_image(car_data, poly_img):
    bb_img = poly_img.copy()
    for index, item in enumerate(car_data):
        if item["type"] == "polygonlabels":
            img_width = item["original_width"]
            img_height = item["original_height"]
            label = item["value"]["polygonlabels"][0]
            xy = get_original_coordinates(item["value"]["points"], img_width, img_height)
            bb_coords = get_bounding_box_coordinates(xy)
            img2 = bb_img.copy()
            draw = ImageDraw.Draw(img2)
            draw.rectangle(xy=bb_coords,outline=item["value"]["outline_color"])
            draw.text(xy=bb_coords[0],text=label,fill="black")
            bb_img = Image.blend(bb_img, img2, 1)
    return bb_img


def get_json_data(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
        return data


