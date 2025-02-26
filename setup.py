from setuptools import setup, find_packages

setup(
    name="scrap_credit_risk_pipeline",
    version="0.1.0",
    author="Kaushal Choudhary",
    author_email="your_email@example.com",
    description="Smart Credit Risk Analysis Pipeline (SCRAP) using PySpark, GCP, and Databricks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SCRAP-CreditRiskPipeline",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyspark",
        "pandas",
        "numpy",
        "scikit-learn",
        "sqlalchemy",
        "great-expectations",
        "streamlit",
        "apache-airflow",
        "google-cloud-storage",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
