# pytest-template

Welcome to pytest-template, a project template that provides essential files and directories with client utilities (
api_client, db_client, etc.) for using pytest in any projects. This template aims to streamline your testing process by
offering a robust and easy-to-use setup.

## Features

- Ready-to-use client utilities for API and database testing.
- Dependencies used in this template are safe and optimized for fast execution.
- Platform-independent; no dependencies on any specific operating system.
- Easy installation and setup process.
- Simple configuration: all you need to do is add domains for tests as directories and create fixtures as Python files
  in the fixtures directory.

## Installation

To get started with pytest-template, follow these simple steps:

1. Clone the repository:
    - ``` git clone https://github.com/amaym0n/pytest-template.git ```
2. Change into the project directory:

    - ``` cd pytest-template ```
3. Install the required dependencies:
    - ``` pip install --upgrade pip ```
    - ``` pip install poetry ```
    - ``` poetry install ```

## Getting Started

1. Add your test domains as directories and add their helpers inside. For example:

    ``` 
   domain_name/
    ├── helpers/
        └── domain_helper.py
    └── tests/
        └── test_domain.py
   ```
2. Create your fixtures as `*.py` files inside the `fixtures` directory. These fixtures will be reusable across
   different test modules. For example:
    ```
   fixtures/
    ├── db_fixtures.py
    ├── api_fixtures.py
    └── ...
   ```
3. Add created fixtures as plugins in conftest.py. For example:
    ```conftest.py
    pytest_plugins = [
      "fixtures.db_fixtures",
      "fixtures.api_fixtures",
    ]
   ```

4. Now you are all set to start writing your tests using pytest.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or pull request in
the [pytest-template repository](https://github.com/amaym0n/pytest-template).

Let's make testing with pytest even more seamless together!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms
of the license.

Happy testing with pytest-template!
