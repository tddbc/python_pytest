from acme.fizzbuzz import FizzBuzz
import pytest

class TestFizzBuzz:

    @pytest.fixture()
    def fizzbuzz(self):
        return FizzBuzz()

    def test_1を渡すと文字列1を返す(self, fizzbuzz):
        assert fizzbuzz.convert(1) == '1'

    def test_2を渡すと文字列2を返す(self, fizzbuzz):
        assert fizzbuzz.convert(2) == '2'

    def test_3を渡すと文字列Fizzを返す(self, fizzbuzz):
        assert fizzbuzz.convert(3) == 'Fizz'
