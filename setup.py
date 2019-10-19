import setuptools

setuptools.setup(
    name="miniabm",
    version="0.0.1",
    author="David Naves Sousa",
    author_email="davidnsousa@gmail.com",
    description="Minimalist tool for agent-based modeling in python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/davidnsousa/miniabm",
    packages=["miniabm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires='>=3.6',
)