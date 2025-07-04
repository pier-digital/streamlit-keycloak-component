from pathlib import Path
import setuptools

setuptools.setup(
    name="streamlit-keycloak-component",
    version="0.0.1",
    author="Gideon Bleumink",
    author_email="",
    description="Keycloak authentication for Streamlit",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/pier-digital/streamlit-keycloak-component",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
