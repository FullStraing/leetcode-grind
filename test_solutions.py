"""Tests for every solution in solutions/ — run: python -m unittest -v"""
import unittest

from solutions.binary_search import search
from solutions.container_with_most_water import max_area
from solutions.contains_duplicate import contains_duplicate
from solutions.first_bad_version import first_bad_version
from solutions.group_anagrams import group_anagrams
from solutions.longest_repeating_character_replacement import character_replacement
from solutions.longest_substring import length_of_longest_substring
from solutions.minimum_size_subarray_sum import min_sub_array_len
from solutions.search_insert_position import search_insert
from solutions.sqrt_x import my_sqrt
from solutions.two_sum import two_sum
from solutions.two_sum_ii import two_sum_ii
from solutions.valid_anagram import is_anagram
from solutions.valid_palindrome import is_palindrome
from solutions.valid_parentheses import is_valid
from solutions.min_stack import MinStack
from solutions.evaluate_rpn import eval_rpn
from solutions.daily_temperatures import daily_temperatures
from solutions.asteroid_collision import asteroid_collision
from solutions.remove_adjacent_duplicates import remove_duplicates
from solutions.decode_string import decode_string
from solutions.backspace_compare import backspace_compare
from solutions.simplify_path import simplify_path


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


class TestMinimumSizeSubarraySum(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_single_element(self):
        self.assertEqual(min_sub_array_len(4, [1, 4, 4]), 1)

    def test_no_subarray(self):
        self.assertEqual(min_sub_array_len(11, [1, 1, 1, 1, 1]), 0)


class TestSearchInsertPosition(unittest.TestCase):
    def test_found(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 5), 2)

    def test_between(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 2), 1)

    def test_ends(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 7), 4)
        self.assertEqual(search_insert([1, 3, 5, 6], 0), 0)


class TestFirstBadVersion(unittest.TestCase):
    def test_middle(self):
        self.assertEqual(first_bad_version(5, lambda v: v >= 4), 4)

    def test_first_is_bad(self):
        self.assertEqual(first_bad_version(1, lambda v: True), 1)

    def test_last_is_bad(self):
        self.assertEqual(first_bad_version(3, lambda v: v >= 3), 3)


class TestSqrtX(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(my_sqrt(4), 2)

    def test_rounds_down(self):
        self.assertEqual(my_sqrt(8), 2)

    def test_small(self):
        self.assertEqual(my_sqrt(0), 0)
        self.assertEqual(my_sqrt(1), 1)

    def test_large(self):
        self.assertEqual(my_sqrt(2147395599), 46339)


class TestValidParentheses(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid("()[]{}"))

    def test_wrong_type(self):
        self.assertFalse(is_valid("(]"))

    def test_wrong_order(self):
        self.assertFalse(is_valid("([)]"))

    def test_nested(self):
        self.assertTrue(is_valid("{[]}"))


class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def test_abab(self):
        self.assertEqual(character_replacement("ABAB", 2), 4)

    def test_aababba(self):
        self.assertEqual(character_replacement("AABABBA", 1), 4)

    def test_no_replacements(self):
        self.assertEqual(character_replacement("AAAA", 0), 4)

    def test_abbb(self):
        self.assertEqual(character_replacement("ABBB", 2), 4)

class TestMinStack(unittest.TestCase):
    def test_basic_flow(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        self.assertEqual(s.get_min(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.get_min(), -2)

    def test_min_updates(self):
        s = MinStack()
        s.push(5)
        s.push(1)
        s.push(4)
        self.assertEqual(s.get_min(), 1)
        s.pop()
        s.pop()
        self.assertEqual(s.get_min(), 5)

    def test_single(self):
        s = MinStack()
        s.push(7)
        self.assertEqual(s.top(), 7)
        self.assertEqual(s.get_min(), 7)

class TestEvaluateRPN(unittest.TestCase):
    def test_add_mul(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)

    def test_div_add(self):
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)

    def test_truncates_toward_zero(self):
        self.assertEqual(eval_rpn(["-13", "5", "/"]), -2)
        self.assertEqual(eval_rpn(["13", "-5", "/"]), -2)

    def test_long_expression(self):
        self.assertEqual(
            eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
            22)

class TestDailyTemperatures(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0])

    def test_increasing(self):
        self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])

    def test_single(self):
        self.assertEqual(daily_temperatures([30]), [0])

    def test_decreasing(self):
        self.assertEqual(daily_temperatures([90, 80, 70]), [0, 0, 0])

class TestAsteroidCollision(unittest.TestCase):
    def test_smaller_explodes(self):
        self.assertEqual(asteroid_collision([5, 10, -5]), [5, 10])

    def test_equal_explode(self):
        self.assertEqual(asteroid_collision([8, -8]), [])

    def test_chain_collision(self):
        self.assertEqual(asteroid_collision([10, 2, -5]), [10])

    def test_no_collisions(self):
        self.assertEqual(asteroid_collision([-2, -1, 1, 2]), [-2, -1, 1, 2])

class TestRemoveAdjacentDuplicates(unittest.TestCase):
    def test_abbaca(self):
        self.assertEqual(remove_duplicates("abbaca"), "ca")

    def test_azxxzy(self):
        self.assertEqual(remove_duplicates("azxxzy"), "ay")

    def test_chain(self):
        self.assertEqual(remove_duplicates("aababaab"), "ba")

    def test_none(self):
        self.assertEqual(remove_duplicates("abc"), "abc")

class TestDecodeString(unittest.TestCase):
    def test_two_groups(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")

    def test_nested(self):
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")

    def test_trailing_plain(self):
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_multi_digit(self):
        self.assertEqual(decode_string("10[a]"), "a" * 10)

class TestBackspaceCompare(unittest.TestCase):
    def test_equal_after_backspace(self):
        self.assertTrue(backspace_compare("ab#c", "ad#c"))

    def test_both_empty(self):
        self.assertTrue(backspace_compare("ab##", "c#d#"))

    def test_not_equal(self):
        self.assertFalse(backspace_compare("a#c", "b"))

    def test_leading_backspaces(self):
        self.assertTrue(backspace_compare("a##c", "#a#c"))

class TestSimplifyPath(unittest.TestCase):
    def test_trailing_slash(self):
        self.assertEqual(simplify_path("/home/"), "/home")

    def test_above_root(self):
        self.assertEqual(simplify_path("/../"), "/")

    def test_dots_and_doubles(self):
        self.assertEqual(simplify_path("/home//foo/./bar/../baz"), "/home/foo/baz")

    def test_double_up(self):
        self.assertEqual(simplify_path("/a/./b/../../c/"), "/c")


if __name__ == "__main__":
    unittest.main()
