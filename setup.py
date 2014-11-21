from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as np

NAME = "eudaq2np"
VERSION = "0.1"
DESCR = "A simle script to get data from EUDAQ"
URL = "https://github.com/SiLab-Bonn/eudaq2np"
REQUIRES = ['numpy', 'cython']

AUTHOR = "Tomasz Hemperek"
EMAIL = "hemprek@uni-bonn.de"

LICENSE = "Apache 2.0"

SRC_DIR = "eudaq2np"
PACKAGES = [SRC_DIR]

ext_1 = Extension(SRC_DIR + ".wrapped",
                  [SRC_DIR + "/lib/cfunc.cxx", SRC_DIR + "/wrapped.pyx"],
                  language = "c++",
		  extra_compile_args=["-std=c++11"],
		  libraries=["EUDAQ"],
		  include_dirs=[np.get_include()])


EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )
