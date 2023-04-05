# TDDBC for Python with Pytest

これは、TDDBC の Pythonista 向け [Pytest](http://pytest.org/latest-ja/) プロジェクトです。

## 動作確認環境

- Python 3.11.1

## セットアップ

以下のように実行して、環境を構築してください。

```:sh
git clone https://github.com/shingotakagij7a/python_pytest.git
cd python_pytest
poetry install
```

テストを実行するには pytest コマンドを使います。

```:sh
poetry run pytest
...

# Output sample

============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /root/work/python_pytest, configfile: setup.cfg
plugins: forked-1.3.0, cov-2.11.1, xdist-2.2.1
collected 5 items

tests/acme/test_snake.py::test_python_hisses PASSED                      [ 20%]
tests/acme/test_snake.py::TestMontyPython::test_say_name_guido PASSED    [ 40%]
tests/acme/test_snake.py::TestMontyPython::test_say_name_kent PASSED     [ 60%]
tests/acme/test_snake.py::TestMontyPython::test_say_name[Terry-Hello Terry] PASSED [ 80%]
tests/acme/test_snake.py::TestMontyPython::test_say_name[John-Hello John] PASSED [100%]

============================== 5 passed in 0.05s ===============================
```

のように正常終了すれば OK です。

## ライセンス

MIT
