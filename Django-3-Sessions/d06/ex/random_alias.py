from d06 import settings

import random


def random_alias():
    rdint = random.randint(0, 9)
    return settings.ANONIMOUS_ALIASES[rdint]
