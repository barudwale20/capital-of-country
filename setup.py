from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="find-capital",
    version="1.0.0",
    author="Shubham Barudwale",
    author_email="barudwale20@gmail.com",
    description="find-capital package",
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        find-capital-cli=capital_finder.run:main
    ''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barudwale20/capital-of-country",
    include_package_data=True,
    data_files=[("capital_finder/resources", ["capital_finder/resources/capital.json"])],
    classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyfiglet==0.8.post1"
    ],

)
