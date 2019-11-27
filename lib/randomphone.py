import random
def randomphone():
    ran_str = ''.join(random.sample('0123456789', 4))
    return ran_str

def randomtime():
    h = ''.join(random.sample('012', 2))
    m = ''.join(random.sample('0123456', 2))
    ran_str = h+":"+m
    return ran_str


