from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Reads requirements from requirements.txt file"""
    requirements:List[str]= []
    try:
        with open('requirements.txt') as f:
            lines=f.readlines()
            for line in lines:
                requirement= line.strip()
                if requirement and requirement!='-e .':
                    requirements.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    return requirements

setup(
    name='network_security',
    author='SPS',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements()
)


   