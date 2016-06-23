from distutils.core import setup

setup(
    name = "luckysearch",
    version = "1.0.0",
    description = "A small search library.",
    author = 'Lucky Sithole',
    author_email = 'luckysithole92@gmail.com.com',
    long_description=open('README.rst', 'r').read(),
    py_modules = [
        'luckysearch'
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
    ],
    url = 'https://github.com/lnsithol/luckysearch'
)
