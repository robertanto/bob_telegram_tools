import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bob-telegram-tools",  # Replace with your own username
    version="1.0.0",
    author="Antonio Roberto",
    author_email="roberto.antonio@outlook.it",
    description="A package to monitor your Machine Learning trainings every where without any additional app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonioroberto1994/bob_telegram_tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.9.2',
        'matplotlib>=2.0.0',
        'tqdm>=4.11.2',
        'python-telegram-bot'
    ],
)
