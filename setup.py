import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mwahpy-donlot", # Replace with your own username
    version="0.1.0",
    author="Tom Donlon",
    author_email="donlot@rpi.edu",
    description="A python package for easily parsing and processing data from milkyway@home",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomasdonlon/mwahpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.2.3',
    install_requires=[
        "numpy",
        "galpy",
        "matplotlib",
        "random",
        "astropy",
        "scipy",
        "math",
        "unittest"
        ],
)