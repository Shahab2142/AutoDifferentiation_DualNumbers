from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name="dual_autodiff_cython",
    version="0.1.0",
    packages=["dual_autodiff_cython"],
    ext_modules=cythonize(
        [
            Extension("dual_autodiff_cython.dual", ["dual_autodiff_cython/dual.pyx"]),
            Extension("dual_autodiff_cython.version", ["dual_autodiff_cython/version.pyx"]),
        ],
        compiler_directives={"language_level": "3"},  
    ),
    package_data={"dual_autodiff_cython": ["*.so"]},  
    include_package_data=True,  
    zip_safe=False,
)
