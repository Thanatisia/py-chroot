# CONTRIBUTING

## Table of Contents
+ [Rules](#rules)
+ [Distribution and Packaging](#distribution-and-packaging)

## Rules
### Open Source Contribution
- Create a fork/branch to your contribution
- Open Pull Request to request to merge your updates into the 'development' branch
    - Please specify your contribution details in the following in your Pull Request
        + Title: `[category] : [summary]`
        - Body:
            ```
            Author Name: [your-name]
            Files Modified:
                - Files changed here
            Reason/Motivation:
            Summary:
                - Your changes here
            ```
+ Do not force merge directly to the main branch

## Setup
### Pre-Requisites
- Clone repository
    ```console
    git clone https://github.com/Thanatisia/py-chroot
    ```

- Change directory into repository
    ```console
    cd py-chroot
    ```

- Initialize submodules
    ```console
    git submodule update --init
    ```

- (Optional) Create Virtual Environments for isolation testing/usage
    - Create the Virtual Environment container
        ```console
        python -m venv env
        ```
    - Chroot and enter Virtual Environment
        - Linux
            ```console
            . env/bin/activate
            ```
        - Windows
            ```console
            .\env\Scripts\activate
            ```

- Change directory into project root directory
    ```console
    cd [project-root-directory]
    ```

## Distribution and Packaging
### Development and Testing
- Install framework using pip
    - Locally as development mode
        ```console
        pip install .
        ```

### Build
#### Using setuptools
- Build/Compile static files
    - Explanation
        + This will compile/"package" the source files into an 'egg', .tar and wheel static files for sharing and installation
    ```console
    python setup.py build
    ```

### Installation
- Local installation
    - Install built static files using setup.py with setuptools
        - Explanation
            + This will install all dependencies, pre-requisites using setup.py and install the framework/package defined in setup.py
        ```console
        python setup.py install
        ```
    - Install built static distribution files
        - tarball
            ```console
            pip install dist/[package-name]-[version-number].tar.gz
            ```
        - wheel
            ```console
            pip install dist/[package-name]-[version-number]-[python-version].whl
            ```
        - egg file
            ```console
            pip install dist/[package-name]-[version-number]-[python-version].egg
            ```

- Remote installation
    - Install from GtiHub
        ```console
        pip install git+https://github.com/Thanatisia/py-chroot{@[branch-tag-name]}
        ```

### Confirmation
- Validate package is installed
    ```console
    pip freeze list
    ```

### Post-Installation
- Uninstall package
    ```console
    pip uninstall [package-name]
    ```

## Resources

## References

## Remarks

