from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gpustatapi',
    description='Simple API Wrapper for gpustat',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yueyericardo/gpustatapi',
    author='Richard Xue',
    license='Apache License 2.0',
    author_email='yueyericardo@gmail.com',
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'gpustat',
    ],
    entry_points={
        'console_scripts': ['gpustatapi = gpustatapi:main'],
    },
)
