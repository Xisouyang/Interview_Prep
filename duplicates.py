# duplicates.py

'''Given two lists of variable size, sorted, find all duplicates of the two lists

input: [1, 2, 3, 4], [2, 5, 7, 1]
output: [2, 1]
'''

def returnDupe(arrOne, arrTwo):
    if len(arrOne) == 0 or len(arrTwo) == 0:
        return
    result = []

    # brute
    # for i in range(len(arrOne)):
    #     for j in range(len(arrTwo)):
    #         if arrTwo[j] == arrOne[i]:
    #             if arrOne[i] in result:
    #                 pass
    #             else:
    #                 result.append(arrOne[i])
    # return result

    my_dict = {}
    for i in range(len(arrOne)):
        my_dict[arrOne[i]] = 1
    for i in range(len(arrTwo)):
        # check to see if the array item exists in dictionary
        if arrTwo[i] in my_dict:
            my_dict[arrTwo[i]] += 1
            if my_dict[arrTwo[i]] > 2:
                pass
            else:
                result.append(arrTwo[i])
    return result


def main():
    arrayOne = [1,2, -3, 3, 4]
    arrayTwo = [1, 2, 3, 6, 9, 3, -3, -3]
    result = returnDupe(arrayOne, arrayTwo)
    print(result)



if __name__ == '__main__':
    main()
