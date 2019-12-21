from day08.ImageReader import ImageReader


if __name__ == "__main__":
    with open("data/full_image", "r") as fh:
        image_reader = ImageReader(fh.read(), (6, 25))
    print(image_reader.image)
