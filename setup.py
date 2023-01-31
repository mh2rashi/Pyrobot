from setuptools import setup
from setuptools import find_namespace_packages

# load the README file.
with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(

    name='trad-robo-python',

    author='Hamza Rashid',

    author_email='hamza022697@gmail.com',

    version='1.0.6',

    description='A trading robot written in Python utilizing the Lemon Markets API capable of maintaining a portfolio\
                of instruments, displaying performance metrics, submitting orders, providing real-time & historical\
                data and showcasing technical indicators.',

    long_description=long_description,

    long_description_content_type="text/markdown",

    url='https://github.com/mh2rashi/Trad-Robo-Python',

    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'requests'
    ],

    keywords='finance, lemon markets, api, trading robot',

    packages=find_namespace_packages(
        include=['pyrobot']
    ),

    include_package_data=True,

    python_requires='>=3.8',

    classifiers=[

        # I can say what phase of development my library is in.
        'Development Status :: 3 - Alpha',

        # Here I'll add the audience this library is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',

        # Here I'll define the license that guides my library.
        'License :: OSI Approved :: MIT License',

        # Here I'll note that package was written in English.
        'Natural Language :: English',

        # Here I'll note that any operating system can use it.
        'Operating System :: OS Independent',

        # Here I'll specify the version of Python it uses.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',

        # Here are the topics that my library covers.
        'Topic :: Database',
        'Topic :: Education',
        'Topic :: Office/Business'

    ]
)