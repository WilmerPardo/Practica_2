class BinarySecuencial():
    def binary_primitive_secuencial(self, array, data, low, high):
        if low > high:
            return []
        mid = (low + high) // 2
        result = []
        if array[mid] == data:
            result.append(array[mid])
        if mid + 1 <= high:
            result += self.binary_primitive_secuencial(array, data, mid + 1, high)
        if mid - 1 >= low:
            result += self.binary_primitive_secuencial(array, data, low, mid - 1)
        return result
            #return self.binary_primitive_secuencial(array, data, low, mid - 1)
