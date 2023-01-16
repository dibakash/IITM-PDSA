# IITM-PDSA

A repository for Lectures and concepts from IIT Madras PDSA (Programing, Data Structures and Algorithm) and related concepts for in-depth understanding of DSA

## Technical Setup

### Use Python built-in virtual environment venv

- Setup virtual environment

  ```
  python -m venv .venv
  ```

- Activate virtual environment
  ```
  source .venv/Scripts/activate
  ```
- To Deactivate virtual environment
  ```
  deactivate
  ```

### Custom Packages

- maintain packages under "my_packages" folder.
- use "poetry" package manager to build additional packages to be installed in the virtual environment

### Using Performance package

- Install the Performance Package

  ```
  pip install my_packages\Performance
  ```

- Importing Performance module
  ```
  from Performance import Performance
  ```
