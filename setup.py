from setuptools import setup, find_packages

setup(
    name="snipgen",
    version="0.1.0",
    author="Christophe Schevers",
    author_email="christophe.schevers@gmail.com",
    description="A tool for generating VS Code snippets from clipboard text.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ChristopheSchevers/vs-snippet-generator",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "pyperclip",
        "tkinter",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)