# Struct-Maker

**Struct=Maker** is a command-line tool that automates the creation of folder structures for new projects. It allows you to quickly set up the basic folder and file structure for software projects, ensuring organization and consistency from the start.

## Features

- Automatically creates folders and subfolders commonly used in projects.
- Flexible configuration for different types of projects (web, API, scripts, etc.).
- Generates base files like `.gitignore` and `README.md`.
- Easy to use and configure.

## Installation

You can install* **Struct-Maker* via `pip`:

```bash
pip install structmaker

Usage

After installation, you can create the folder structure for your new project with the following command:

bash

structmaker create my_new_project

This will create the following folder structure inside the my_new_project directory:

plaintext

my_new_project/
│
├── src/
│   ├── assets/
│   ├── components/
│   ├── services/
│   ├── utils/
│   ├── styles/
│   ├── config/
│   ├── models/
│   ├── views/
│   └── main.*
│
├── public/
│   ├── index.html
│   └── ...
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── ...
│
├── build/
│   └── ...
│
├── docs/
│   └── ...
│
├── scripts/
│   └── ...
│
├── .gitignore
├── README.md
└── ...

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on the GitHub repository.
License

This project is licensed under the MIT License.