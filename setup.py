from setuptools import setup, find_packages

setup(
    name='python_ondc',
    version='0.0.1',
    license='MIT',
    author="Krishna",
    author_email='info@vambook.in',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    keywords='ondc adaptor',
    install_requires=[],
)
