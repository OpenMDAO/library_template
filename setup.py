from distutils.core import setup
from setuptools import find_packages

setup(name='your_project',
    version='1.0.0',
    description='description',
    url='https://github.com/your-org/your_project',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache 2.0',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    license='Apache License',
    packages=find_packages(),
    install_requires=[
        'openmdao>=3.8.0',
        'numpy>=1.20.2',
        'scipy>=1.6.2',
        'six',
        'pep8',
        'parameterized',
        'sphinx',
        'sphinxcontrib-bibtex',
        'redbaron',
        'jupyter-book',
        'testflo'
    ],
    zip_safe=False,
)
