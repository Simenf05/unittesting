import collections.abc as abc


def fizzbuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    if input % 3 == 0:
        return "buzz"
    if input % 5 == 0:
        return "fizz"
    
    
def selection_sort(array):
    
    if not isinstance(array, abc.MutableSequence):
        raise (TypeError("Typen er ikke mutable"))
    
    
    if not isinstance(array, abc.Iterable):
        raise (TypeError("Typen kan ikke itereres"))
    
    array.sort()
    return array

if __name__ == "__main__":
    print(selection_sort([3, 8, 4, 12, 1]))