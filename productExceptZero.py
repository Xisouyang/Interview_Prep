# Given array of integers, return an array of integers s.t. the value at index
# i of the output is the product of everything in the input except the element at i.
# input: [1, 2, 0, 4] => [0, 0, 8, 0]
# [1, 2, 3, 4] => [24, 12, 8, 6]

def main(array):
    new_array = []
    product = 1

    # n + n^2 = O(n^2) overall
    # condition = 0 in array  # O(n)
    # if condition:  # O(1)
    if 0 in array:  # O(n) but only evaluated once. Check for 0s
    # while condition:  # O(1)
    # while 0 in array:  # O(n) and evaluated each iteration
        # O(n^2)
        for i in range(len(array)): # Check for 0's position
            if array[i] == 0: # found where 0 is
                for j in range(len(array)): # multiply all numbers in array to product, unless 0.
                    if array[j] == 0:
                        product = product + array[j] # Add 0 bc we don't want it affecting the product
                    else:
                        product = product * array[j]
                new_array.append(product)
                product = 1
            else:
                new_array.append(0)
        print(new_array)
    else:
        for i in range(len(array)):
            product = 1
            for j in range(len(array)):
                product = product * array[j]
            product = product / array[i]
            new_array.append(product)
        print(new_array)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        numbers = map(int, sys.argv[1:])
    else:
        numbers = [-1, -1, -1, -1, -1]
    main(numbers)
