def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Collector:
    def __init__(self):
        pass


c_a = Collector()
c_b = Collector()
print(c_a == c_b)
