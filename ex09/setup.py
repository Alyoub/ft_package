from setuptools import setup, find_packages


setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    author="alotfi",
    author_email="alotfi@42.fr",
    url="https://github.com/alyoub/Project-1",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
