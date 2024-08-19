from setuptools import setup, find_packages

setup(
    name='struct-maker',
    version='0.1.0',
    description='A command-line tool for automating project folder structure creation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lucas Americo',
    author_email='lucasamerico695@tutamail.com',
    url='https://github.com/lucasamerico/struct-maker',  # Update this with your actual repository URL
    packages=find_packages(),
    install_requires=[
        "os>=1.0"
    ],
    entry_points={
        'console_scripts': [
            'struct-maker=struct_maker.main:main',  
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/lucasamerico/struct-maker#readme',  
        'Source': 'https://github.com/lucasamerico/struct-maker',  
    },
)
