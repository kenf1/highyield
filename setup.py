from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory/"README.md").read_text()

setup(name="highyield",
      version="1.0.4",
      description="Collection of high-yield functions intended to simplify and automate specific tasks.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/kenf1/High-Yield",
      author="KF",
      author_email="kenfv1@outlook.com",
      license="GPLv3",
      package_data={"highyield": ["data/*.csv"]},
      packages=find_packages(where="highyield"),
      include_package_data=True,
      python_requires=">=3.8",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
      ],
      install_requires=[
        "pandas",
        "pyttsx3",
        "docx2pdf",
        "pypdf"
      ],
      zip_safe=False)