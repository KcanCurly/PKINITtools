from setuptools import setup, find_packages

setup(
    name="pkinittools",
    version="1.0.0",
    author="KcanCurly",
    description="A script to dump files and folders remotely from a Windows SMB share.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/PKINITtools",
    packages=find_packages(),
    install_requires=[
        "minikerberos",
        "oscrypto @ git+https://github.com/wbond/oscrypto",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "getnthash.py=src.getnthash:main",  
            "gets4uticket.py=src.gets4uticket:main", 
            "gettgtpkinit.py=src.gettgtpkinit:main", 
        ],
    },
)