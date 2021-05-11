import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Color-Theories",
    version="0.1.5",
    author="Augusto Nunes Zacarias",
    author_email="augusto.zacarias@ccc.ufcg.edu.br",
    description="A simple coloring game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/augustonz/Color-Theories",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'ColorTheories=ColorTheories.main:run'
            ]
        }
)
