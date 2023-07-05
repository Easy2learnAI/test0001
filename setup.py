from setuptools import setup

with open("README.MD", "r") as fh:
    description = fh.read()
    
setup(
    name="test_pkg",
    version="0.1.0",
    description=description,
    author="Mohammed Tahar",
    author_email="hydconcept00@gmail.com",
    url = "https://github.com/Easy2learnAI/test_pkg",
    license = "MIT",
    modules = "main" 
)
