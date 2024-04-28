import numpy as np
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import setup

ext_modules = [
]

setup(
    name="cyml",
    version="0.0.1",
    packages=["cyml"],
    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize(module_list=ext_modules,
                          language_level=3,
                          annotate=True,
                          compiler_directives={
                              "boundscheck": False,
                              "wraparound": False,
                          }),
    include_dirs=[np.get_include()]
)