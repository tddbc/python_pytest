from acme.fizzbuzz import FizzBuzz

class TestFizzBuzz:

    def test_1を渡すと文字列1を返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行 & 検証
        assert fizzbuzz.convert(1) == '1'

    def test_2を渡すと文字列2を返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行 & 検証
        assert fizzbuzz.convert(2) == '2'
