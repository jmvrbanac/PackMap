"""
Copyright 2014 John Vrbanac

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import argparse
import json

from pkg_resources import get_distribution

all_requires = {}


def get_requires(package_name):
    reqs = []
    dist = get_distribution(package_name)

    for req in dist.requires():
        reqs.append({
            'name': req.project_name,
            'spec': ''.join([''.join(t) for t in req.specs])
        })

    return dist.version, reqs


def get_all_requires(package_name):
    version, reqs = get_requires(package_name)

    pack = all_requires.get(package_name, {})
    temp_reqs = pack.get('requirements', [])

    # Only include new packages
    for req in reqs:
        if req not in temp_reqs:
            temp_reqs.append(req)

    all_requires[package_name] = {
        'version': version,
        'requirements': temp_reqs
    }

    for req in reqs:
        get_all_requires(req.get('name'))


def main(*args, **kwargs):
    """ Simple entry-point that takes the package name and json output"""

    parser = argparse.ArgumentParser()
    parser.add_argument('package_name', type=str)
    parser.add_argument('output_filename', type=str)

    parsed_args = parser.parse_args()

    # Find all package requirements
    get_all_requires(parsed_args.package_name)

    # Write tmp results to a file to be read into main app context
    json_file = open(parsed_args.output_filename, 'w')
    json_file.write(json.dumps(all_requires))


if __name__ == '__main__':
    main()
