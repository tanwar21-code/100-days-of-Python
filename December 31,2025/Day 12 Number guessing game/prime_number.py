def is_prime(num):
    count = 0
    for i in range(2,num):
        if num %i == 0:
            count += 1
        else:
            continue
    if count == 0:
        return True
    else:
        return False

is_prime(73)
