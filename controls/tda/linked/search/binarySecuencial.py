from controls.tda.linked.linkedList import Linked_List
from controls.tda.linked.search.binary import Binary

class BinarySecuencial(Binary):
    def binary_ascendent(self, array, data, low, high, positions=None):
        if positions is None:
            positions = Linked_List()

        mid = super().binary_ascendent(array, data, low, high)
        if mid != -1:
            positions.add(mid)

        return positions

    def binary_descendent(self, array, data, low, high, positions=None):
        if positions is None:
            positions = Linked_List()

        mid = super().binary_descendent(array, data, low, high)
        if mid != -1:
            positions.add(mid)

        return positions