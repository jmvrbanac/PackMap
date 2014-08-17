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

from packmap import env


class PackMapClient(object):

    def __init__(self):
        self.args = None
        self.parser = self.build_arguments(argparse.ArgumentParser())

    def parse_args(self):
        self.args = self.parser.parse_args()
        return self.args

    def build_arguments(self, parser):
        # TODO(jmv) Add a way to specify install type
        # parser.add_argument('install_type', type=str)

        # Required Args
        parser.add_argument('package_name', type=str)

        # Options
        parser.add_argument('--keep-env', action='store_true')

        return parser


def main(*args, **kwargs):
    client = PackMapClient()
    parsed_args = client.parse_args()

    builder = env.EnvironmentBuilder()
    builder.build()

    builder.install_package(parsed_args.package_name)

    if not parsed_args.keep_env:
        builder.clean_up()

if __name__ == '__main__':
    main()
