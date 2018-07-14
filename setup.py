from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author='Steven Delaney',
    author_email='stevenddelaney@gmail.com',
    description='Snapshotalyzer 30000 is a tool to manage ec2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/sddelaney/snapshotalyzer-3000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
