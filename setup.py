from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]


setup(
    name="AI-Enhanced-Image-Restoration",
    version="8.14.1",
    author="Utso Sarkar",
    author_email="utsosarkar1@gmail.com",
    description="AI-powered image enhancement using RealESRGAN and GFPGAN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/officiallyutso/AI-Enhanced-Image-Restoration",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 19 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "enhance-image=examples.enhance_image:main",
        ],
    },
)