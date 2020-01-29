import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_oferbaharav", # Replace with your own username
    version="0.0.2",
    author="Ofer Baharav",
    author_email="oferbaharav@gmail.com",
    description="practice uploading and playing around with pipy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oferbaharav/lambdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)