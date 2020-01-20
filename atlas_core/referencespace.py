class Referencespace:
    """Representation of a referencespace with name and a list of parcellations"""
    name = None
    parcellations = None

    def __init__(self, name, parcellations):
        self.name = name
        self.parcellations = parcellations

    def __str__(self):
        return "(name: {0})".format(self.name)

    def __repr__(self):
        return self.__str__()
