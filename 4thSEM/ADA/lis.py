
def binarySearch(sub, val):
    low, high = 0, len(sub)-1
    while(low <= high):
        mid = low + (high - low)//2
        if sub[mid] < val:
            low = mid + 1
        elif val < sub[mid]:
            high = mid - 1
        else:
            return mid
    return low


def lengthOfLIS(nums):
    sub_sequence = []
    for val in nums:
        pos = binarySearch(sub_sequence, val)
        if pos == len(sub_sequence):
            sub_sequence.append(val)
        else:
            sub_sequence[pos] = val
    return len(sub_sequence)


lengthOfLIS([int(j) for j in input('Enter numbers: ').split()])
