TDDBC for Python with Pytest
============================

これは、TDDBCのPythonista向け Pytest_ プロジェクトです

.. _Pytest: http://pytest.org/latest-ja/

動作確認環境
------------

- Python 2.7.6
- Python 3.3.1
- PyPy 1.9.0
- PyPy 2.2.0

セットアップ
------------

.. code-block:: sh

   $ pip install -r requirements.txt

**setup.py** を実行し

.. code-block:: sh

   $ python setup.py test
   
   ...
   
   # Output sample
   ======================== test session starts =================================
   platform linux2 -- Python 2.7.3[pypy-2.2.0-final] -- pytest-2.4.2
   -- ~/.virtualenvs/tddbc_python_pytest_pypy22/bin/python
   plugins: cov, xdist
   collected 3 items
   
   tests/acme/test_acme.py:28: TestPython.test_be_out_of_question PASSED
   tests/acme/test_acme.py:41: TestMontyPython.test_say_name[Monty Python] PASSED
   tests/acme/test_acme.py:41: TestMontyPython.test_say_name[John Smith] PASSED
   ======================== 3 passed in 0.10 seconds ============================

のように正常終了すればOKです

ライセンス
----------

MIT ライセンスです (詳しくはプロジェクト直下の LICENSE をご覧ください)
