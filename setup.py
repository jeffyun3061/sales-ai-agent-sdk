from setuptools import setup, find_packages
import setuptools

setup(
    name='leadscout_sdk',
    version='0.1.0',
    description='LeadScout AI SDK for Sales Scouting',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(where="leadscout_sdk"),
    package_dir={"": "leadscout_sdk"},
    install_requires=[
        'pymysql',
        'boto3',
        'pdfminer.six',
        'openai',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
