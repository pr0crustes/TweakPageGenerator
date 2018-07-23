'''
Copyright [2018] [pr0crustes (https://github.com/pr0crustes)]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import os


class Generator:

    def __init__(self):

        self.id = input("Enter the tweak id [com.me.mytweak]:")
        self.name = input("Enter the tweak name [MyTweak]:")

        self.version = input("Enter the tweak version [0.0.1-1]:")

        self.changelog = input("Enter the tweak changelog [fixing bugs]:")
        self.mini = input("Enter the lowest ios compatible [11.1.X]:")
        self.maxi = input("Enter the highest ios compatible [12.X.X]:")
        self.other = input("Versions not in this interval are `unsupported` or `unconfirmed`?")
        self.dependencies = input("Enter your tweak dependencies [preferenceloader]:")
        self.description = input("Enter your tweak description [a good tweak]:")

        self.base_path = self.id + "/"
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

        self.link_name = None
        self.link_url = None

        if input("Want to include a link? (Y, N)").lower().rstrip() == "y":
            self.link_name = input("Enter the link name [source code]:")
            self.link_url = input("Enter the url [https://some.link.here]:")

    def generate_changelog_file(self):
        with open(self.base_path + "changelog.xml", "w") as file:
            file.write("<changelog>\n"
                       "\t<changes>\n"
                       "\t\t<version>{}</version>\n"
                       "\t\t<change>{}</change>\n"
                       "\t</changes>\n"
                       "</changelog>\n".format(self.version, self.changelog))

    def get_headers(self):
        return "\t<id>{}</id>\n" \
               "\t<name>{}/name>\n" \
               "\t<version>{}</version>\n".format(self.id, self.name, self.version)

    def get_compatibility(self):
        return "\t<compatibility>\n" \
               "\t\t<firmware>\n" \
               "\t\t\t<miniOS>{}</miniOS>\n" \
               "\t\t\t<maxiOS>{}</maxiOS>\n" \
               "\t\t\t<otherVersions>{}</otherVersions>\n" \
               "\t\t</firmware>\n" \
               "\t</compatibility>\n".format(self.mini, self.maxi, self.other)

    def get_dependencies(self):
        return "\t<dependencies>{}</dependencies>\n".format(self.dependencies)

    def get_description(self):
        return "\t<descriptionlist>\n" \
               "\t\t<description>{}</description>\n" \
               "\t</descriptionlist>".format(self.description)

    def get_changelog(self):
        return "\t<changelog>\n" \
               "\t\t<change>{}</change>\n" \
               "\t</changelog>\n".format(self.changelog)

    def get_links(self):
        return "\t<links>\n" \
               "\t\t<name>{}</name>\n" \
               "\t\t<url>{}</url>\n" \
               "\t</links>\n".format(self.link_name, self.link_url)

    def get_info(self):
        return "".join(["<package>\n",
                        self.get_headers(),
                        self.get_compatibility(),
                        self.get_dependencies(),
                        self.get_description(),
                        self.get_changelog(),
                        self.get_links(),
                        "</package>\n"])

    def generate_info_file(self):
        with open(self.base_path + "info.xml", "w") as file:
            file.write(self.get_info())


if __name__ == '__main__':

    gen = Generator()

    gen.generate_changelog_file()
    gen.generate_info_file()

