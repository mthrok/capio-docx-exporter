"""Install Capio Word Exporter Command line"""
import setuptools


def _setup():
    setuptools.setup(
        name='capio_word_exporter',
        version='0.0.1',
        packages=setuptools.find_packages(exclude=['tests']),
        test_suite='tests',
        install_requires=[
            'requests',
            'python-docx',
        ],
        entry_points={
            'console_scripts': [
                'capio_word_exporter = capio_word_exporter.main:main'
            ]
        }
    )


if __name__ == '__main__':
    _setup()
