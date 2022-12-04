def syntax_error(some_list):

    return sorted(some_list)


def sem_error(x, y):

    return (str(x) + y)


def logical_error(count):
    x = 0
    if count > x:
        x += 1
    return x


if __name__ == '__main__':
    syntax_error([3,2,1])
    sem_error(5, "test")
    logical_error(8)
