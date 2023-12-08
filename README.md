<div align="center">
    <h1 align="center">
        <img src=./media/download.png width="150" >
<br>Swarm CID</h1>

<p align="center">

<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff" alt="Python" />
  <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=for-the-badge&logo=Poetry&logoColor=white" alt="Poetry" />

<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="Pytest" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/aviksaikat/swarm-cid-py.svg">
  <img src="https://img.shields.io/github/forks/aviksaikat/swarm-cid-py.svg">
  <img src="https://img.shields.io/github/issues/aviksaikat/swarm-cid-py.svg">
</p>

<p align="center">
 <img src = "https://img.shields.io/badge/python-3.9+-blue.svg">
  <img src ="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"/>
  <img src ="https://img.shields.io/badge/imports-isort-17DE93.svg" alt="imports: isort"/>
  <img src = "https://www.mypy-lang.org/static/mypy_badge.svg">
</p>

<img src="https://img.shields.io/github/license/Aviksaikat/swarm-cid-py?style=for-the-badge&color=DEDE17" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/Aviksaikat/swarm-cid-py?style=for-the-badge&color=DEDE17" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/Aviksaikat/swarm-cid-py?style=for-the-badge&color=DEDE17" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/Aviksaikat/swarm-cid-py?style=for-the-badge&color=DEDE17" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 API](#-Api)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running swarm-cid-py](#-running-swarm-cid-py)
  - [🧪 Tests](#-tests)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📍 Api

Utility library written in Python to convert Swarm hex references into Swarm CIDs.

The swarm-cid library provides the following functions:

`encode_reference(reference, type, version)`

Encodes a reference string into a CID.

- reference: The reference string to encode.
- type: The type of the reference (either ReferenceType.MANIFEST or ReferenceType.FEED).
- version: The version of the CID (either 1 or 2).
  Returns a CID string.

`decode_cid(cid)`

Decodes a CID string into a dictionary containing information about the underlying data.

- cid: The CID string to decode.

Returns a dictionary with the
following keys:

- reference: The reference string extracted from the CID.
- type: The type of the reference (either ReferenceType.MANIFEST or ReferenceType.FEED).

`decode_feed_cid(cid)`

Decodes a CID string into a feed reference string.

- cid: The CID string to decode.
  Returns a feed reference string.

`decode_manifest_cid(cid)`

Decodes a CID string into a manifest reference string.

- cid: The CID string to decode.
  Returns a manifest reference string.

`encode_feed_reference(reference)`

Encodes a feed reference string into a CID.

- reference: The feed reference string to encode.
  Returns a CID string.

`encode_manifest_reference(reference)`

Encodes a manifest reference string into a CID.

- reference: The manifest reference string to encode.

---

## 🚀 Getting Started

**_Dependencies_**

```py
py-multiformats-cid
```

---

### 🔧 Installation

```sh
pip install swarm_cid_py
```

---

### 🤖 Running swarm-cid-py

```py
>>> from swarm_cid import encode_reference, decode_cid
>>> reference = "4c949794d617238d928ef1dc544ee07cbdcfd6b946e5202fa06c4d32088d7e69"
>>> cid = encode_reference(reference, ReferenceType.MANIFEST, 1)
>>> print(str(cid))
bah5acgzajskjpfgwc4ry3euo6hofitxaps647vvzi3ssal5anrgtecenpzuq
>>> decoded_cid = decode_cid(cid)
>>> print(decoded_cid.to_dict())
{'reference':
'4c949794d617238d928ef1dc544ee07cbdcfd6b946e5202fa06c4d32088d7e69', 'type': 'manifest'}
```

---

### 🧪 Tests

```sh
pytest tests/test_swarm_cid.py
```

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Aviksaikat/swarm-cid-py/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Aviksaikat/swarm-cid-py/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Aviksaikat/swarm-cid-py/issues)**: Submit bugs found or log feature requests for ETHERSPHERE.

#### _Contributing Guidelines_

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License

This project is protected under the [BSD-3-Clause](./LICENSE) License.

[**Return**](#Top)

---
