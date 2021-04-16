class FizzBuzz:
    def convert(self, n):
        return '1'

class TestFizzBuzz:
    def test_1を渡すと文字列1を返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行 & 検証
        assert fizzbuzz.convert(1) == '1'
