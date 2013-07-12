from testdata import everything as things


def get_item(the_id):
    for thing in things:
        if thing["id"]==the_id:
            return thing
    return None

def extract_items(key, value):
    return [ x for x in things if x[key]==value ]


def select(f):
    return [ x for x in things if f(x) ]
