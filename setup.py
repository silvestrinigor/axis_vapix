from setuptools import setup, find_packages

setup(
    name="axis_vapix",
    version="0.2.11",
    description="Python-based API handler for interacting with Axis devices using the VAPIX APIs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Igor da Silva Silvestrin",
    author_email="silvestrinigor@icloud.com",
    url="https://github.com/silvestrinigor/axis_vapix",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=["requests==2.32.3", "packaging==24.2", "pytz==2024.2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires=">=3.10"
)