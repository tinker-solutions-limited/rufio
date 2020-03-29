from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install
from shutil import copyfile
import os.path

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        if (not os.path.isfile("./.env")):
            print("creating .env")
            copyfile("./shadow.env", "./.env")

setup(name='rufio',
    version='0.0.1',
    description='Lookie Lookie I Got Hookie.',
    url='https://github.com/tinker-solutions-limited/rufio',
    author='Tinker Solutions Limited',
    author_email='',
    license='GNU General Public License v3.0',
    packages= find_packages("serve"),
    cmdclass={
        'install': PostInstallCommand,
    },
    install_requires=[
    'Flask', 'python-dotenv'
    ],
    zip_safe=False
)