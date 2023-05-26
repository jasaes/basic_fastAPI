class Pokemon:

    def __init__(self):
        print('Constructor called.')


    def __init__(self, name, id=None, types=None, stats=None):
        if id is None:
            self.name = name
        else:
            self.id = id
            self.name = name
            self.species = [name]
            self.types = types
            self.stats = stats
        print('Constructor called.')


