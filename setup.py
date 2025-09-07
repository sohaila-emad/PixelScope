#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="pixelscope",
    version="1.0.0",
    author="Sohaila Emad",
    author_email="sohaila.emad@example.com",  # Update with your email
    description="An advanced image viewer and processing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sohaila-emad/PixelScope",
    project_urls={
        "Bug Tracker": "https://github.com/sohaila-emad/PixelScope/issues",
        "Documentation": "https://github.com/sohaila-emad/PixelScope/wiki",
        "Source Code": "https://github.com/sohaila-emad/PixelScope",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.910",
            "pytest-cov>=2.12",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "pixelscope=main:main",  # Adjust this based on your main file structure
        ],
        "gui_scripts": [
            "pixelscope-gui=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords=[
        "image-processing",
        "computer-vision", 
        "opencv",
        "tkinter",
        "gui",
        "image-analysis",
        "roi-analysis",
        "medical-imaging",
        "signal-processing",
        "noise-analysis",
    ],
    zip_safe=False,
)
