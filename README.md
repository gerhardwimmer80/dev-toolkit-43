# dev-toolkit-43

`dev-toolkit-43` is a robust Python-based CLI utility designed to streamline repetitive local development workflows. It bridges the gap between common shell tasks and complex script automation, providing a unified interface for project maintenance.

## Features

*   **Project Scaffolding:** Rapidly generate standardized directory structures and configuration files for new Python projects.
*   **Environment Sync:** Automatically synchronize dependency files and local environment variables across multiple development machines.
*   **Log Sanitizer:** A built-in regex-based tool to scrub sensitive information from production log exports before local analysis.
*   **Task Runner:** Execute pre-defined build hooks and cleanup sequences with simple, cross-platform terminal commands.

## Installation

Ensure you have Python 3.9 or higher installed. Install the package directly via pip:

```bash
pip install dev-toolkit-43
```

Alternatively, for local development:

```bash
git clone https://github.com/developer/dev-toolkit-43.git
cd dev-toolkit-43
pip install -e .
```

## Usage

Once installed, you can access the toolkit via the `dt43` command. Use the following command to initialize a new configuration file in your current directory:

```bash
dt43 init --type web-app
```

To clean your logs and run a build sequence simultaneously, use the pipe operation:

```bash
dt43 clean ./logs && dt43 build --production
```

For a full list of available modules and flags, run:

```bash
dt43 --help
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.