from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="pyinnovativetrend",
    version="0.2",
    packages=find_packages(),
    description="An innovative trend analysis and visualization tool",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    author="Md Mehedi Hasan Prodhan",
    author_email="mehediprodhan1613@outlook.com",
    keywords="time series analysis, trend analysis, innovative trend, trend, ITA, ita",
    python_requires=">=3.7, <4",
    install_requires=["numpy","pandas","matplotlib","scipy"]
)