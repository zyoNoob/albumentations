from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    "numpy>=1.24.4",
    "scipy>=1.10.0",
    "PyYAML",
    "typing-extensions>=4.9.0; python_version<'3.10'",
    "pydantic>=2.9.2",
    "albucore @ git+https://github.com/zyoNoob/albucore.git",
    "eval-type-backport; python_version<'3.10'",
    "opencv-python>=4.9.0.80",
]

setup(
    packages=find_packages(exclude=["tests", "tools", "benchmark"], include=['albumentations*']),
    install_requires=INSTALL_REQUIRES,
)