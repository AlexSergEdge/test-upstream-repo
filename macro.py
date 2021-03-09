from animals import horse
import animals
import sys

# test
# test2

def cat(sound):
    return 'Cat says {}'.format(sound)

def dog(sound):
    return 'Dog says {}'.format(sound)

def monkey(sound):
    return 'Monkey says {}'.format(sound)

if hasattr(sys.modules[__name__], 'dog'):
    res = getattr(sys.modules[__name__], 'dog')("Bow")
    print(res)
else:
    print('Not found')

lname = "cat"

# Если функция находится в этом же файле
res = globals()[lname]('Meou')
print(res)

gname = "horse"

# Если функция находится в другом файле (animals например)
res = getattr(animals, gname)("Igogogo")
print(res)


    