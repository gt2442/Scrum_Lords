# setup.py
from setuptools import setup

setup(
    name="RecipeMatcher",
    version="0.1",
    description="A simple BeeWare app for Recipe Matching",
    author="Your Name",
    packages=["RecipeMatcher"],
    install_requires=["toga", "httpx"],  # Add other dependencies if needed
    entry_points={
        'toga': [
            'RecipeMatcher = RecipeMatcher:main'
        ]
    }
)
