class Referencespace:
    """Representation of a referencespace with name and a list of parcellations"""
    name = None
    id = None
    parcellations = None

    def __init__(self, name, id, parcellations):
        self.name = name
        self.id = id
        self.parcellations = parcellations

    def __str__(self):
        return "(name: {0}, id: {1})".format(self.name, self.id)

    def __repr__(self):
        return self.__str__()
