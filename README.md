# Python Virtual Environment

A virtual environment has been created in the `venv` directory. This allows you to install Python packages in an isolated environment without affecting your system Python installation.

## Activating the Virtual Environment

### On macOS/Linux:
```bash
source venv/bin/activate
```

### On Windows:
```bash
.\venv\Scripts\activate
```

## Deactivating the Virtual Environment

When you're done working in the virtual environment, you can deactivate it by running:
```bash
deactivate
```

## Installing Packages

After activating the virtual environment, you can install packages using pip:
```bash
pip install package_name
```

## Creating Requirements File

To save a list of installed packages:
```bash
pip freeze > requirements.txt
```

## Installing from Requirements File

To install packages from a requirements file:
```bash
pip install -r requirements.txt
```
