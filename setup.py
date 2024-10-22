# setup.py

from setuptools import setup, find_packages

setup(
    name="mqtt_trigger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "paho-mqtt",
        "json"
    ],
    author="FAH",
    author_email="",
    description="An MQTT-based tool to trigger on value changes and condition. Makes code extremely short.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fah/mqtt-trigger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
