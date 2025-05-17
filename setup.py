from setuptools import setup, find_packages

setup(
    name="zara",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "aiohttp",
        "lxml"
    ],
    entry_points={
        "console_scripts": [
            "zara=zara.cli:main"
        ]

    },
    author="upliftedl",
    description="Fast, extensible username enumeration tool",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8"
)
