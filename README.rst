***************************************************
PackMap - Python Package Dependency Finding Utility
***************************************************

PackMap is a simple utility which finds all packages required by a given Python package. It does this by installing the package and all of its dependencies into a clean temporary virtual environment and probing installed components for their actual requirements.

* |PYPI| **GitHub:** `jmvrbanac/PackMap <https://github.com/jmvrbanac/PackMap>`_

.. |PYPI| image:: https://badge.fury.io/py/packmap.svg
	:target: http://badge.fury.io/py/packmap

Installation:
==============
PackMap is available on PyPI and can be installed with pip:
	pip install packmap


Usage:
=======

Checking the dependencies of a package on PyPI:
	packmap lplight --pdf-results

Checking the dependencies of a package on your hard drive:
	packmap lplight --install-type path --install-path /path/to/package --pdf-results


Results:
=========

PackMap output's two different type of results; JSON and PDF.

* JSON results: Gives you the ability to parse through the results for yourself to find changes in version numbers or requirement specs.
* PDF results: Produces an graph for easier viewing and consumption.

.. note::
	The PDF results functionality requires the graphviz system package to be installed.
