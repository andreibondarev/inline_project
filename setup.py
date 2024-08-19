from setuptools import setup, find_packages

setup(
    name='inline-project',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'inline-project=inline_project:main',
        ],
    },
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to inline project content into a single file',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/inline-project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

