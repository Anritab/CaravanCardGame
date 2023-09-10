from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='caravanassets',
    version='0.0.2',
    description='This is a python package for implementing the card game Caravan',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Anri Tabuev',
    author_email='anri.tabuev@gmail.com',
    keywords=['caravan', 'card', 'cardgame', 'game', "fallout"],
    url='https://github.com/Anritab/CaravanCardGame',
    download_url='https://github.com/Anritab/CaravanCardGame/issues'
)

if __name__ == '__main__':
    setup(**setup_args)