import random


def get_random_winners(quantity, participants):

    list_keys =[]
    for i in participants.keys():
        list_keys.append(i)
    if quantity > len(participants): return [] 
    random.shuffle(list_keys)
    result = random.sample(list_keys, k=quantity)
    return result