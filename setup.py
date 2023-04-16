from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',
    version='1',
    description='This module will sort your folder.'
    url='https://github.com/TurMod/clean_folder'
    author='Mykhailo Gordiichuk',
    author_email='turbo.moderator@gmail.com',
    license='Apache Software',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:launch_script']}
)