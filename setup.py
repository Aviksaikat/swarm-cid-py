from setuptools import find_packages, setup

setup(
    name="bee-py",
    version="0.1.0",
    description="Python client library for connecting to Bee decentralised storage",
    author="Saikat Karmakar",
    author_email="saikickkarma@protonmail.com",
    license="AGPL-3.0-or-later",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alienrobotninja/bee-py",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "eth-ape",
        "ape-alchemy",
        "ape-solidity",
        "ape-foundry",
        "ape-etherscan",
        "pyscaffold",
        "cryptography",
        "coverage-enable-subprocess",
        "pytest-cov",
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
        ],
        "lint": [
            "black>=23.9.1,<24",  # Auto-formatter and linter
            "mypy>=1.5.1,<2",  # Static type analyzer
            "types-PyYAML",  # Needed due to mypy typeshed
            "types-requests",  # Needed due to mypy typeshed
            "types-setuptools",  # Needed due to mypy typeshed
            "pandas-stubs==1.2.0.62",  # Needed due to mypy typeshed
            "types-SQLAlchemy>=1.4.49",  # Needed due to mypy typeshed
            "flake8>=6.1.0,<7",  # Style linter
            "flake8-breakpoint>=1.1.0,<2",  # detect breakpoints left in code
            "flake8-print>=4.0.1,<5",  # detect print statements left in code
            "isort>=5.10.1,<6",  # Import sorting linter
            "mdformat>=0.7.17",  # Auto-formatter for markdown
            "mdformat-gfm>=0.3.5",  # Needed for formatting GitHub-flavored markdown
            "mdformat-frontmatter>=0.4.1",  # Needed for frontmatters-style
            # headers in issue templates
            "mdformat-pyproject>=0.0.1",  # Allows configuring in pyproject.toml
            # "pyproject-flake8>=6.1.0",  # need to connect pyproject.toml config to flake8
        ],
    },
)
