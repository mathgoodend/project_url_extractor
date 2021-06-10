from setuptools import setup

setup(
    name = 'Url Extractor',
    version = '1.0.0',
    packages = ['url_extractor'],
    entry_points = {
        'console_scripts': [
            'url_extractor = url_extractor.__main__:main'
        ]
    }
)