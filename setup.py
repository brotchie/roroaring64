import os
from setuptools import setup, Extension
from Cython.Build import cythonize

VERSION = "0.1.0"

USE_CYTHON = os.path.exists("roroaring64.pyx")


def find_sources():
    """Finds all CRoaring source files."""
    sources = []
    for dirpath, _, filenames in os.walk("CRoaring/src"):
        for filename in filenames:
            if filename.endswith(".c"):
                sources.append(os.path.join(dirpath, filename))
    return sources


# If we're going to compile from scratch, then use the Cython
# source, otherwise we're likely being built from the dist package
# downloaded by pip so we're safe to compile from the Cython
# C++ output.
target = "roroaring64.pyx" if USE_CYTHON else "roroaring64.cpp"
extension = Extension(
    "roroaring64",
    sources=[target] + find_sources(),
    include_dirs=["CRoaring/include", "CRoaring/cpp"],
)

if USE_CYTHON:
    ext_modules = cythonize(
        extension,
        compiler_directives={"language_level": "3"},
    )
else:
    ext_modules = [extension]

with open("README.md", "rb") as f:
    long_description = f.read().decode("utf-8")

setup(
    name="roroaring64",
    ext_modules=ext_modules,
    version=VERSION,
    description="Deserializer for 64 bit Roaring Bitmaps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brotchie/roroaring64",
    author="James Brotchie",
    author_email="brotchie@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
