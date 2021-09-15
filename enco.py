import math


class ShannonFano:
    def __init__(self, sorted_probabilities, sorted_source):
        self.sorted_probabilities = sorted_probabilities
        self.sorted_source = sorted_source
        self.length_of_source = len(self.sorted_source)
        self.encoded = ['1', '0']
        self.encode()

    def encode(self):
        def get_array(arr):
            sum_arr = sum(arr)
            s = 0
            array1 = []
            array2 = []
            for i in arr:
                s += i
                if sum_arr / 2 >= s or len(array1) == 0:
                    array1.append(i)
                else:
                    array2.append(i)
            return [array1, array2]

        result = get_array(self.sorted_probabilities)

        index = 0

        while index <= len(self.sorted_probabilities) - 1:
            i = result[index]
            if len(i) > 1:
                result.remove(i)
                x, y = get_array(i)
                result.insert(index, x)
                result.insert(index + 1, y)
                x = self.encoded[index]
                self.encoded.remove(x)
                self.encoded.insert(index, x + '1')
                self.encoded.insert(index + 1, x + '0')
            else:
                index += 1

    @staticmethod
    def self_info(p):
        return math.log2(1 / p)

    def entropy(self):
        return sum([i * self.self_info(i) for i in self.sorted_probabilities])

    def average_length(self):
        return sum([i * len(self.encoded[index]) for index, i in enumerate(self.sorted_probabilities)])

    def get_results(self):
        print('Symbol\t', 'Probabilities\t', 'Code')
        for i in range(self.length_of_source):
            print(self.sorted_source[i], '\t\t', self.sorted_probabilities[i], '\t\t\t', self.encoded[i])
        print('Avglength : ', self.average_length(), '\t\t', 'Entropy: ', self.entropy(), '\t\t', 'Redundancy:',
              self.redundancy())

    def redundancy(self):
        return 1 - self.entropy() / self.average_length()


sorted_probabilities = [0.13, 0.091, 0.082, 0.075, 0.07, 0.067, 0.063, 0.061, 0.06, 0.043, 0.04,
                        0.028, 0.028, 0.024, 0.024, 0.022, 0.02, 0.02,
                        0.019, 0.015, 0.0098, 0.0077, 0.0015, 0.0015, 0.00095, 0.00074]

sorted_source = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
                 'V', 'K', 'J', 'X', 'Q', 'Z']
obj = ShannonFano(sorted_probabilities, sorted_source)
obj.get_results()
