from setuptools import setup, find_packages

setup(
    name="enterprise-ecommerce-backend",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.110.0",
        "uvicorn==0.28.0",
        "pyyaml==5.1",
        "requests==2.31.0",
        "pyjwt==1.7.1",
        "pydantic==2.6.4",
        "pytest==8.1.1",
    ],
)
