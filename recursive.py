def f(num, aList = []):
    if num == 0:
        return aList
    aList.insert(0, num * num)
    return f(num - 1, aList)


def main():
    result = f(10)
    print(result)

if __name__ == '__main__':
    main()
