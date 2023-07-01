from setuptools import setup, find_packages


setup(
    name='nanorequests',
    version='0.7',
    license='MIT',
    author="Viral Parmar",
    description='The simplest REST requests package for quick API integration',
    author_email='viralparmarme@gmail.com',
    packages=['src'],
    url='https://github.com/viralparmarme/nanorequests',
    keywords='src viralparmarme viralparmar',
    py_modules=['nanorequests', 'exceptions'],
    install_requires=[
        'requests'
    ],
)
