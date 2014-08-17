from setuptools import setup, find_packages

setup(
    name='packmap',
    version='0.0.1',
    description=('PackMap discovers all dependencies for a specific'
                 'Python package'),
    long_description=(''),
    url='',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='discover package dependencies graph',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'packmap = packmap.cli:main'
        ],
    },
)
