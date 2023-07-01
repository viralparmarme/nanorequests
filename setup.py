from setuptools import setup, find_packages


setup(
    name='nanorequests',
    version='0.1',
    license='MIT',
    author="Viral Parmar",
    author_email='viralparmarme@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/viralparmarme/nanorequests',
    keywords='nanorequests viralparmarme viralparmar',
    install_requires=[
        'requests'
    ],
)
