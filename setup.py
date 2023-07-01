from setuptools import setup, find_packages


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
    long_description="README.md",
    long_description_content_type="text/markdown",
    install_requires=[
        'requests'
    ],
)
