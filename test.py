# test.py
def say(world):
    result = 'defult'
    if world == 'a':
        result = 'hello '+world
    elif world == 'b':
        result = 'hello'
    else:
        result = ''
    return result

