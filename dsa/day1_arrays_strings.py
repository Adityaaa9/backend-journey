#  Reverse String
# Input: s = ["h","e","l","l","o"]   → Output: ["o","l","l","e","h"]
# Input: s = ["H","a","n","n","a","h"] → Output: ["h","a","n","n","a","H"]

def reverse_string(s: list[str]) -> None:
    # Time: O(n) | Space: O(1)  — in place, no new list
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]   # Python tuple swap, no temp var
        left += 1
        right -= 1


if __name__ == "__main__":
    a = ["h", "e", "l", "l", "o"]
    reverse_string(a)
    print(a)          # ['o', 'l', 'l', 'e', 'h']

    b = ["H", "a", "n", "n", "a", "h"]
    reverse_string(b)
    print(b)          # ['h', 'a', 'n', 'n', 'a', 'H']

    c = ["x"]
    reverse_string(c)
    print(c)          # ['x']   ← edge case: single element, loop never runs

    d = []
    reverse_string(d)
    print(d)          # []      ← edge case: empty list

"""
 Valid Palindrome
# Input: s = "A man, a plan, a canal: Panama"  → True
#         (cleaned: "amanaplanacanalpanama")
# Input: s = "race a car"                      → False
#         (cleaned: "raceacar")
# Input: s = " "                               → True   (cleaned: "", empty is palindrome)

def is_palindrome(s: str) -> bool:
    # Time: O(n) | Space: O(1)  — skips non-alnum without building a new string
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                      # False
    print(is_palindrome(" "))                               # True
    print(is_palindrome("0P"))                              # False  ← '0' vs 'p'
    print(is_palindrome("ab_a"))                            # True   ← underscore is skipped

"""

"""
 Remove Duplicates from Sorted Array
 # Input: nums = [1,1,2]              → k = 2, nums = [1,2,_]
# Input: nums = [0,0,1,1,1,2,2,3,3,4] → k = 5, nums = [0,1,2,3,4,_,_,_,_,_]
def remove_duplicates(nums: list[int]) -> int:
    # Time: O(n) | Space: O(1)  — write pointer, read pointer
    if not nums:
        return 0
    slow = 0                      # last index holding a unique value
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1               # count of uniques


if __name__ == "__main__":
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    print(k, nums[:k])        # 2 [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    print(k, nums[:k])        # 5 [0, 1, 2, 3, 4]

    nums = [1]
    k = remove_duplicates(nums)
    print(k, nums[:k])        # 1 [1]   ← edge case

    nums = []
    k = remove_duplicates(nums)
    print(k, nums[:k])        # 0 []    ← edge case

"""