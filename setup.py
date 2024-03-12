from setuptools import setup
import os

wordlist = 'wordlist' + os.sep + 'wordlist.txt'

setup(
    name='sfindpy',
    version='7.0.0',
    description='Domain Inspector Global Audit',
    url='https://github.com/atasky/sfind',
    author='Gianni Amato',
    author_email='guelfoweb@gmail.com',
    license='GPL-3.0',
    packages=['sfind'],
    package_data={"sfind": [wordlist, 'report'],},
    include_package_data=True,
    install_requires=['requests>=2.31.0', 'dnspython>=2.4.2', 'pyOpenSSL>=23.3.0', 'beautifulsoup4>=4.12.3', 'tqdm>=4.66.2'],
    entry_points={
        'console_scripts': [
            'sfindpy=sfind.sfindpy:main',
        ],
    }
)
