from setuptools import setup

setup(
    name="sample_example",
    version='0.1',
    py_modules=['example_2'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        click_example_2=example_2:cli
    ''',
)
