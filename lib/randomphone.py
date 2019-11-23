import random
def randomphone():
    ran_str = ''.join(random.sample('0123456789', 4))
    return ran_str
