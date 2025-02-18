from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dual_autodiff",
    version="0.1.0",
    description="A package for forward-mode automatic differentiation using dual numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shahab Yousef-Nasiri",
    author_email="shahab.n2022@yahoo.com",
    url="https://github.com/Shahab2142/dual_autodiff",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[], 
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
