from setuptools import setup, find_packages

setup(
    name="club_recommendation",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # Specify src as the package directory
    include_package_data=True,
    install_requires=[
        # Add your dependencies here or use 
        'streamlit',
        'pandas',
        'numpy',
         'requirements.txt'
    ],
)
