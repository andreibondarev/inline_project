from setuptools import setup, find_packages

setup(
    name='inline_project',  # Changed from 'inline-project' to 'inline_project'
    version='0.1',
    py_modules=['inline_project'],  # Add this line to specify the module
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
    url='https://github.com/andreibondarev/inline_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


