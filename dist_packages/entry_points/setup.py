import setuptools

setuptools.setup(
    name="calculator",
    version="0.0.1",
    author="Yoav Klein",
    author_email="yoavklein25@gmail.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = ["calculator"],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'add = calculator.console:main',
        ]
    }
)
