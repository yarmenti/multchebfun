from setuptools import setup

setup(
    name='multchebfun',
    version = "0.1",
    author = "Yannick Armenti",
    author_email = "yannick.armenti@gmail.com",
    description = ("An implementation of a multi-dimensional Chebyshev function fitter."),
    license = "MIT",
    keywords = ['Math', 'Chebyshev', 'chebfun',],
	packages=['multchebfun',],
	install_requires=['numpy'],
	classifiers=[
    
    'Development Status :: 3 - Alpha',

    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',

     'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
],
 )