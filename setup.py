from setuptools import setup, find_packages
import os


setup(name="nose-colorxunit",
        version = "0.1.2",
        description = "make unittest formatted and colorful output",
        long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
        license = "APACHE LICENSE VERSION 2.0",
        author = "Lesus",
        author_email = "walkingnine@gmail.com",
        url="https://github.com/walkingnine/colorunit",
        py_modules = ["colorunit"],
        zip_safe = False,
        classifiers = [
            "Development Status :: 2 - Alpha",
            "License :: APACHE LICENSE VERSION 2.0",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: Implementation :: CPython",
            ],
        install_requires = [
            "nose>=0.10",
            "colorama>=0.2.5",
            ],
        entry_points = {
            'nose.plugins.0.10':[
                "colorunit = colorunit:ColorUnit"
                ]
            }
        
        )
