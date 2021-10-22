import os
from setuptools import setup, find_packages

version = '0.1'

install_requires = [
    'http_session',
    'pymemcache >= 3.5.0',
]

tests_require = [
    'pytest',
]

setup(
    name='http_session_memcache',
    version=version,
    description="HTTP session handling using memcache as a backend.",
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.rst")).read()),
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
    ],
    keywords='HTTP, Session',
    author='Souheil Chelfouh',
    author_email='trollfot@gmail.com',
    url='https://github.com/HorsemanWSGI/http_session',
    license_files=(
        'docs/LICENSE.txt',
    ),
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    tests_require=tests_require,
    install_requires=install_requires,
    extras_require={'test': tests_require},
)
