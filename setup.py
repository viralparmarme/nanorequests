from setuptools import setup

setup(
    name='nanorequests',
    version='0.9',
    license='MIT',
    author="Viral Parmar",
    description='The simplest REST requests package for quick API integration',
    author_email='viralparmarme@gmail.com',
    packages=['nanorequests'],
    url='https://github.com/viralparmarme/nanorequests',
    keywords='nanorequests viralparmarme viralparmar',
    py_modules=['nanorequests', 'exceptions'],
    install_requires=[
        'requests'
    ],
)
