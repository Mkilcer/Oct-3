#Input a list of #'s
#Output Concatenated #'s
#from ast import Raise


#def concatenate_numbers(numbers):
#    result = ''.join(str(num) for num in numbers)
#    return result   


# import numberconcatenator
# (Removed invalid and incomplete lines)

def number_concatenator(numbers):
    concatenator = NumberConcatenator(numbers)
    concatenated_result = concatenator.concatenate()
    print(concatenated_result)


#class NumberConcatenator 
class NumberConcatenator:
    def __init__(self, numbers):
        self.numbers = numbers

    def concatenate(self):
        result = ''.join(str(num) for num in self.numbers)
        return result

    def print_concatenation(self):
        concatenated_result = self.concatenate()
        print(concatenated_result)