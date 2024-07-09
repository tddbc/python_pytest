############################
TDDBC for Python with Pytest
############################

これは、TDDBCのPythonista向け Pytest_ プロジェクトです

.. _Pytest: http://pytest.org/latest-ja/

動作確認環境
============

- Python 3.12.4
- pytest 8.2.2

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
   ====================================== test session starts ======================================
   platform linux -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0 -- /usr/local/bin/python
   cachedir: .pytest_cache
   rootdir: /root/python_pytest
   configfile: setup.cfg
   plugins: cov-5.0.0, xdist-3.6.1
   collected 3 items
   
   tests/acme/test_snake.py::TestPython::test_be_out_of_question PASSED                      [ 33%]
   tests/acme/test_snake.py::TestMontyPython::test_say_name[Monty Python] PASSED             [ 66%]
   tests/acme/test_snake.py::TestMontyPython::test_say_name[John Smith] PASSED               [100%]
    
   ======================================= 3 passed in 0.02s =======================================

のように正常終了すればOKです

ライセンス
==========

MIT ライセンスです (詳しくはプロジェクト直下の LICENSE をご覧ください)
