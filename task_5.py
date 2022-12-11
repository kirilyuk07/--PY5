import random
from random import sample
import string

def get_random_password() -> str:
    list_sy = (string.ascii_uppercase + string.ascii_lowercase + string.digits)
    return str(random.sample(list_sy, 8))

print(get_random_password())
# пустая строка