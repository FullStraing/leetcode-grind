"""Tests for every solution in solutions/ — run: python -m unittest -v"""
import unittest

from solutions.binary_search import search
from solutions.container_with_most_water import max_area
from solutions.contains_duplicate import contains_duplicate
from solutions.group_anagrams import group_anagrams
from solutions.longest_substring import length_of_longest_substring
from solutions.two_sum import two_sum
from solutions.two_sum_ii import two_sum_ii
from solutions.valid_anagram import is_anagram
from solutions.valid_palindrome import is_palindrome


class TestTwoSum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_later_pair(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_same_value_twice(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])


class TestValidAnagram(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))

    def test_false(self):
        self.assertFalse(is_anagram("rat", "car"))

    def test_length_mismatch(self):
        self.assertFalse(is_anagram("ab", "a"))


class TestGroupAnagrams(unittest.TestCase):
    def test_groups(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        as_sets = sorted(sorted(g) for g in result)
        self.assertEqual(as_sets, [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])

    def test_empty(self):
        self.assertEqual(group_anagrams([""]), [[""]])


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_missing(self):
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_edges(self):
        self.assertEqual(search([5], 5), 0)
        self.assertEqual(search([5], -5), -1)


class TestContainsDuplicate(unittest.TestCase):
    def test_duplicate(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))

    def test_all_distinct(self):
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_empty(self):
        self.assertFalse(contains_duplicate([]))


class TestLongestSubstring(unittest.TestCase):
    def test_abcabcbb(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_all_same(self):
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    def test_pwwkew(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_empty(self):
        self.assertEqual(length_of_longest_substring(""), 0)


class TestTwoSumII(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(two_sum_ii([2, 7, 11, 15], 9), [1, 2])

    def test_negative(self):
        self.assertEqual(two_sum_ii([-10, -3, 0, 5], -13), [1, 2])


class TestValidPalindrome(unittest.TestCase):
    def test_classic(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("race a car"))

    def test_only_spaces(self):
        self.assertTrue(is_palindrome(" "))

    def test_digits(self):
        self.assertTrue(is_palindrome("1a1"))
        self.assertFalse(is_palindrome("0P"))


class TestContainerWithMostWater(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_two_lines(self):
        self.assertEqual(max_area([1, 1]), 1)

    def test_tall_ends(self):
        self.assertEqual(max_area([4, 3, 2, 1, 4]), 16)


if __name__ == "__main__":
    unittest.main()
