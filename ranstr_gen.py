from random import randint
import pseudo_secrets as pseudo


def generate_str(size,listA):
    ranstr=''.join(pseudo.choice(listA) for psswd in range(size))
    return ranstr

