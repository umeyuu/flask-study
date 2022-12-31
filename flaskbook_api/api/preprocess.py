import torchvision


def image_to_tensor(image):
    image_tensor = torchvision.transforms.functional.to_tensor(image)
    return image_tensor
