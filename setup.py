from setuptools import setup, find_packages

setup(
    name="seagull",
    version="0.1.0",
    author="Nick Stucky-Mack",
    author_email="njsm.technologies@gmail.com",
    description="Diffusion transformers using the Siegel upper half-space",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/njsm-tech/seagull",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="MIT",
    python_requires=">=3.7",
)