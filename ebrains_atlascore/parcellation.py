class Parcellation:
    """Representation of a parcellation with name, referencespace and a list of regions"""
    referencespace = None
    name = None
    id = None
    regions = None

    def __init__(self, name, id, referencespace, regions):
        self.name = name
        self.id = id
        self.referencespace = referencespace
        self.regions = regions

    def __str__(self):
        return "(name: {0}, id: {1})".format(self.name, self.id)

    def __repr__(self):
        return self.__str__()
