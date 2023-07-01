from setuptools import setup, find_packages


setup(
    name='nanorequests',
    version='0.2',
    license='MIT',
    author="Viral Parmar",
    description='The simplest REST requests package for quick API integration',
    author_email='viralparmarme@gmail.com',
    packages=find_packages(),
    url='https://github.com/viralparmarme/nanorequests',
    keywords='nanorequests viralparmarme viralparmar',
    install_requires=[
        'requests'
    ],
)
