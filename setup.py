from setuptools import find_packages, setup
from typing import List

remove_hypen='-e .'
def get_requirements(file_path: str) -> List[str]:
    """This function will return a list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", " ") for req in requirements]
        
        if remove_hypen in requirements:
            requirements.remove(remove_hypen)
        return requirements


setup(
    name="Ml_Project",
    version="0.0.1",
    author="Gabriel Bright",
    author_email="gabbybrght@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
