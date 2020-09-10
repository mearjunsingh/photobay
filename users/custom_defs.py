from django.utils.text import slugify
from photos.models import Camera, Location
from django.shortcuts import get_object_or_404


def unique_slug(table, word):
    original = slugify(word)
    unique = original
    num = 1
    while table.objects.filter(slug=unique).exists():
        unique = '%s-%d' % (original, num)
        num += 1
    return unique


def get_or_create_object(data, table):
    if table == Camera:
        if not Camera.objects.filter(camera=data).exists():
            data_obj = Camera(camera=data, slug=unique_slug(Camera, data))
            data_obj.save()
            return data_obj
        else:
            data_obj = get_object_or_404(Camera, camera=data)
            return data_obj
    elif table == Location:
        if not Location.objects.filter(location=data).exists():
            data_obj = Location(location=data, slug=unique_slug(Location, data))
            data_obj.save()
            return data_obj
        else:
            data_obj = get_object_or_404(Location, location=data)
            return data_obj
    else:
        return None


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))