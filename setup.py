import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wifiPass-propellerpain",
    version="0.0.1",
    author="Pierre Hoffmeister",
    author_email="pierre.git@posteo.de",
    description="Creates a printable QR code version of your wifi password",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phoffmeister/wifiPass",
    packages=setuptools.find_packages(),
    install_requires=[
        'fpdf',
        'qrcode',
        'pillow'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
