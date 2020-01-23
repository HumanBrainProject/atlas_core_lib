class Roi:
    """
    A representation for a 'region of interest'

    """

    def __init__(self, data, region, hemisphere, threshold):
        self._data = data
        self._region = region
        self._hemisphere = hemisphere
        self._threshold = threshold

    def save(self, filename):
        file = filename if filename.endswith(".nii") else filename+".nii"
        with open(file, 'wb') as f:
            f.write(self._data)

    def __str__(self):
        return "Roi(Region = {0})".format(self._region)
        pass

    def __repr__(self):
        return self.__str__()
