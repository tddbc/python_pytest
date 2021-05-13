from setuptools import setup, find_packages

setup(
    name='skeleton_for_pytest',
    version='0.0.2',
    url='https://github.com/tddbc/python_pytest.git',
    author='TDD BaseCamp',
    author_email='tddbc@googlegroups.com',
    description='The skeleton of py.test for python users',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    tests_require=['pytest'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
