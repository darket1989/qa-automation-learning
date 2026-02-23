def shallowEqual(a,b):
    if a == b:
        return True

print(shallowEqual({"id":1, "name": "A"},{"id":1, "name": "A"}))