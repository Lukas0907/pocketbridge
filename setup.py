from setuptools import find_packages, setup

setup(
    name="pocketbridge",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask>=2.0.0",
        "flask-redis",
    ],
    extras_require={
        "style": ["black", "flake8", "isort"],
        "test": ["freezegun", "pytest", "pytest-randomly"],
    },
)
