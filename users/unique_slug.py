from django.utils.text import slugify

def unique_slug(table, word):
    original = slugify(word)
    unique = original
    num = 1
    while table.objects.filter(slug=unique).exists():
        unique = '%s-%d' % (original, num)
        num += 1
    return unique