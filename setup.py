from setuptools import setup, find_packages

setup(
    name='ml-docker',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi==0.104.1',
        'uvicorn==0.24.0.post1',
        'scikit-learn==1.3.2',
        'numpy==1.26.2',
    ],
    extras_require={
        'test': [
            'pytest==7.4.3',
            'httpx==0.25.1',
        ]
    }
)