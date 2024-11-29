from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

extensions = [
    Extension("dual_autodiff.dual", ["dual_autodiff/dual.py"]),
    Extension("dual_autodiff.version", ["dual_autodiff/version.py"]),
]

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
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    zip_safe=False,
    install_requires=[],  # No dependencies since only math is used
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
