from distutils.core import setup

setup(name="nose-colorxunit",
        version = "0.1.1",
        description = "make unittest formatted and colorful output",
        license = "APACHE LICENSE VERSION 2.0",
        author = "Lesus",
        author_email = "walkingnine@gmail.com",
        url="my.oschina.net/swuly302",
        py_modules = ["colorunit"],
        zip_safe = False,
        install_requires = [
            "nose>=0.10",
            ],
        entry_points = {
            'nose.plugins.0.10':[
                "colorunit = colorunit:ColorUnit"
                ]
            }
        
        )
