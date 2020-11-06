
from cat import Cat
from dog import Dog
from registry import registry


cat_type = registry[0]
dog_type = registry[1]

cat = cat_type()
dog = dog_type()

cat.talk()
dog.talk()
print(registry)
