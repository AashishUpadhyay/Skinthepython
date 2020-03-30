import sys

# twosum([2, 7, 11, 15], 9)
# twosum([2, 7, 11, 15], 18)


def twosum(nums, target):
    diffWithTargetAndIndexDictionary = dict()
    for i in range(len(nums)):
        if(nums[i] in diffWithTargetAndIndexDictionary):
            return (diffWithTargetAndIndexDictionary.get(nums[i])[0], i)
        else:
            diff = target - nums[i]
            if(diff in diffWithTargetAndIndexDictionary):
                diffWithTargetAndIndexDictionary[diff].append(i)
            else:
                diffWithTargetAndIndexDictionary[diff] = [i]
    return()


def main(nums, target):
    twosum(nums, target)


if __name__ == '__main__':
    main(sys.argv[0], sys.argv[1])
