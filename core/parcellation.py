class Parcellation:
    """Representation of a parcellation with name, referencespace and a list of regions"""
    referencespace = None
    name = None
    regions = None

    def __init__(self, name, referencespace, regions):
        self.name = name
        self.referencespace = referencespace
        self.regions = regions

    def __str__(self):
        return "(name: {0})".format(self.name)

    def __repr__(self):
        return self.__str__()
