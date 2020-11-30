import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pro_foo",  # Replace with your own username
    version="0.0.1",
    author="Mark Bryant",
    author_email="mark.bryant@aecom.com",
    description="Example for extending geoprocessing through Python modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M-Bryant/SamplePythonToolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
