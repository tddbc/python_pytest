############################
TDDBC for Python with Pytest
############################

これは、TDDBCのPythonista向け Pytest_ プロジェクトです

.. _Pytest: http://pytest.org/latest-ja/

動作確認環境
============

- Python 3.8.5
- pytest 6.2.4

※Python2は2020年1月にサポート終了(EOL)していますので、Python3をご利用ください。

セットアップ
============

以下のように実行して、環境を構築してください。

.. code-block:: sh

   $ git clone https://github.com/yattom/python_pytest.git
   $ cd python_pytest
   $ pip3 install -r requirements.txt

テストを実行するには **pytest** コマンドを使います。

.. code-block:: sh

   $ pytest
   
   ...
   
   # Output sample
   ============================= test session starts ==============================
   platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
   cachedir: .pytest_cache
   rootdir: /root/work/python_pytest, configfile: setup.cfg
   plugins: forked-1.3.0, cov-2.11.1, xdist-2.2.1
   collected 3 items
   
   tests/acme/test_snake.py::TestPython::test_be_out_of_question PASSED     [ 33%]
   tests/acme/test_snake.py::TestMontyPython::test_say_name[Monty Python] PASSED [ 66%]
   tests/acme/test_snake.py::TestMontyPython::test_say_name[John Smith] PASSED [100%]
   
   ============================== 3 passed in 0.04s ===============================

のように正常終了すればOKです

ライセンス
==========

MIT ライセンスです (詳しくはプロジェクト直下の LICENSE をご覧ください)
