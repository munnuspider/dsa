
#Maximum Subarray of size K

def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    window_sum = 0
    left = 0
    for right in range(len(arr)):
        window_sum += arr[right]
        if (right - left + 1) == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[left]
            left += 1
    return max_sum


def longest_substring(s):
    max_chars = 0
    char_set = set()
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_chars = max(max_chars, right - left + 1)
    return max_chars


print(longest_substring("abbcdeafddcbcbba"))

from collections import Counter

def find_all_anagrams_in_string(s, p):
    counter_p = Counter(p)
    window_counts = Counter()
    result = []
    left = 0
    k = len(p)
    for right in range(len(s)): # traverse through larger string
        window_counts[s[right]] += 1
        if right - left + 1 == k:
            if window_counts == counter_p:
                result.append(left)

            window_counts[s[left]] -= 1 # decrement count
            if window_counts[s[left]] == 0:
                del window_counts[s[left]]
            left += 1
    return result

print(find_all_anagrams_in_string('baacbac','abc'))


def remove_duplicates(nums):
   i = 0
   for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
   return i + 1, nums[: i + 1]


def unique_triplets(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and (nums[i] == nums[i - 1]):
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                result.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                while (left < right) and (nums[left] == nums[left - 1]):
                    left += 1

            elif sum < 0:
                left += 1
            else:
                right -= 1
    return result

print(unique_triplets(nums = [-1, 1, 0, 2, -1, -4]))

def two_sum_II(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return (left, right)
        elif sum < 0:
            left += 1
        else:
            right -= 1
    return nums 


class node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class solution:
    def has_cycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def start_of_cycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

    




