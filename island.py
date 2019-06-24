'''Given a 2d array of ones and zeros, where ones represent islands and zeroes represent water,
find the width and height of the island if there can only be one island. Island is rectangular.

input: [[
0, 0, 0, 0
0, 1, 1, 0
0, 1, 1, 0
0, 1, 1, 0
]]

output: width => 2
        height => 3

'''

def main():

    input = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
    ]

    width = 0
    height = 0
    checked = False

    # traverse through 2D array
    # once you find a 1, check its neighbors. As long as neighbor isn't 0, keep going.
    # once you find a 0, you can start traversing downwards because you know it
    # has to be a rectangle.


    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 1 and checked == False:
                checked = True
                width += 1
                k = j + 1
                while k <= len(input[i]) - 1 and input[i][k] != 0:
                    width += 1
                    k += 1
                k -= 1
                l = i
                while l <= len(input) - 1 and input[l][k] != 0:
                    height += 1
                    l += 1

    print("width: {}".format(width))
    print("height: {}".format(height))


if __name__ == '__main__':
    main()
