from setuptools import setup, find_packages

setup(
    name="generative_ai_solutions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "transformers",
    ],
    author="Krishna Pandey",
    description="Enterprise-grade Generative AI Solutions",
)