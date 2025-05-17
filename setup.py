from setuptools import setup, find_packages

setup(
    name="zara",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["aiohttp", "lxml"],
    entry_points={
        "console_scripts": [
            "zara=cli:main"
        ]
    },
    author="upliftedl",
    description="Fast, extensible username enumeration tool",
    license="MIT"
)
