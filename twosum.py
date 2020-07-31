from collections import OrderedDict
# Very slow for large data sets!

def main():
    data = []
    with open('2sum.txt') as file:
        for line in file.readlines():
            data.append(int(line.strip()))

    # sort and remove duplicates
    data_arr = list(OrderedDict.fromkeys(data)) 
    data_arr.sort()
    data_set = set(data_arr)

    # result = 0
    # for i in range(-10000, 10001):
    #     if twoSumCheck(data_set, i):
    #         result += 1
    # print(result)

    result = 0
    for i in range(-10000, 10001):
        if twoSumCheck_2(data_arr, i):
            result += 1
    print(result)

    # num_set = {4, 5, 1, 8, 3, 5, 7, 2, 1}
    # print(num_set)
    # target = 9
    # result = 0
    # for i in range(11):
    #     sums = twoSum(num_set, i)
    #     result += len(sums)
    #     print(sums)
    # print(result)

    # result = 0
    # for i in range(11):
    #     if twoSumCheck(num_set, i):
    #         print(i)
    #         result += 1
    # print(result)

    # result = 0
    # num_arr = list(num_set)
    # for i in range(11):
    #     if twoSumCheck_2(num_arr, i):
    #         result += 1
    # print(result)
    

# # check if there is a pair of number that sums up to target, return true at the first pair found
# # using sorted arrays
def twoSumCheck_2(num_arr, target):
    i = 0
    j = len(num_arr) - 1
    while i < j:
        value = num_arr[i] + num_arr[j]
        if value == target:
            return True
        elif value < target:
            i += 1
        else: 
            j -= 1
    return False


# check if there is a pair of number that sums up to target, return true at the first pair found
# using sets
def twoSumCheck(num_set, target):
  
    for num in num_set:
        complement = target - num
        if complement in num_set:
            if complement != num:
                return True
            
    return False


# checks for every possible pair that sums up to target and returns the list
def twoSum(num_arr, target):
    sums = []
    seen = set()

    for num in num_arr:
        complement = target - num
        if complement in seen:
            if complement != num:
                sums.append((complement, num))
                seen.remove(complement)
        else:
            seen.add(num)

    return sums


if __name__ == "__main__":
    main()