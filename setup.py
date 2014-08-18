from setuptools import setup, find_packages

requirements = ['virtualenv', 'pyparsing==1.5.7', 'pydot==1.0.2']

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='packmap',
    version='0.0.1',
    description=('PackMap discovers all dependencies for a specific'
                 'Python package'),
    long_description=(desc),
    url='https://github.com/jmvrbanac/PackMap',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Topic :: Utilities'
    ],
    keywords='discover package dependencies graph dependency requirement',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'packmap = packmap.cli:main'
        ],
    },
)
