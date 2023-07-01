from setuptools import setup, find_packages


setup(
    name='nanorequests',
    version='0.5',
    license='MIT',
    author="Viral Parmar",
    description='The simplest REST requests package for quick API integration',
    author_email='viralparmarme@gmail.com',
    url='https://github.com/viralparmarme/nanorequests',
    keywords='nanorequests viralparmarme viralparmar',
    py_modules=['nanorequests'],
    install_requires=[
        'requests'
    ],
)
