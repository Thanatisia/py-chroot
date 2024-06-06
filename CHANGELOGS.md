# Changelogs

## Table of Contents
+ [2024-06-05](#2024-06-05)
+ [2024-06-06](#2024-06-06)

## Entries

### 2024-06-05
#### 2135H
+ Initial Commit

+ Version: v0.1.0

- New
    + Added new document 'README.md'
    + Added new document 'CHANGELOGS.md'
    + Added new document '.gitignore'
    + Added new document 'requirements.txt'
    + Added new document 'CONTRIBUTING.md'
    + Added the python package configuration file 'pyproject.toml'
    - Added new directory 'docs/' for documentations
        + Added new resource Makefile 'documentation.Makefile' : Makefile for starting asciinema/agg to record demo animation gifs for the project
    - Added new directory 'src/' for all source codes and files
        - Added new directory 'pychroot' : The main py-chroot package
            - Added new directory 'repl' : Contains the REPL source codes
                + Added new file 'main.py'

### 2024-06-06
#### 0947H
- Updates
    - Updated entry point source code for the REPL 'main.py' in 'src/pychroot/repl/'
        + Refactor: Created new functions and refactored to make the code cleaner

#### 1001H
- New
    + Added new document 'FEATURES.md' for all Features in the pipelines

#### 1003H
- Updates
    - Updated document 'FEATURES.md'
        + Added new TODO entry into the pipeline

#### 1017H
- Updates
    - Updated document 'README.md'
        + Added motivation and project information

#### 1654H
- New
    - Added new directory 'core' in 'src/pychroot/' for containing modules/libraries related to the chroot core functionalities
        - Added new directory 'chroot/' for module/libraries involving chroot functions
            - Added new directory 'linux/' for Linux-specific functionalities
                + Added new module 'chroot.py'
            - Added new directory 'windows/' for Windows-specific functionalities
                + Added new module 'chroot.py'
    - Added new directory 'utils' in 'src/pychroot' for generic utilities that will be used by the package
        - Added new module/library directory 'io/' containing modules/libraries related to Input/Output (IO) Processing and Handling operations
            + Added new module 'files.py' related to File-related I/O Processing and Handling
        - Added new module/library directory 'system/' containing modules/libraries related to the Operating System/Platform
            + Added new module 'platform.py' : Wrapper/helper library that is built on top of the 'platform' module
- Updates
    - Updated entry point source code for the REPL 'main.py' in 'src/pychroot/repl/'
        + Separated functions to related modules for customizability and modularity
        + Added platform checking for cross-platform compatibility
        + Added baseline for command history
        + Added data validation: Null Value check
        + Added PROMPT customization (WIP)
        + REPL/shell infrastructure working

#### 1730H
- Updates
    - Updated entry point source code for the REPL 'main.py' in 'src/pychroot/repl/'
        - Implemented customizable REPL/shell prompt using 'eval()' to format strings including the use of built-in python source code
            + TODO: Identify alternatives for customizable prompts

#### 2015H
- Updates
    - Updated document 'README.md'
        + Updated parameters and options
    - Updated entry point source code for the REPL 'main.py' in 'src/pychroot/repl/'
        + Implemented CLI argument parsing supported
        + Added optional arguments for customizing the root filesystem mount point and root directory using CLI arguments

#### 2335H
+ Version: v0.2.0

- Version Changes
    - Feature Changes
        - Updated entry point source code for the REPL 'main.py' in 'src/pychroot/repl/'
            + Refactor: Created new functions and refactored to make the code cleaner
            + Separated functions to related modules for customizability and modularity
            + Added platform checking for cross-platform compatibility
            + Added baseline for command history
            + Added data validation: Null Value check
            + Added PROMPT customization (WIP)
            + REPL/shell infrastructure working
            - Implemented customizable REPL/shell prompt using 'eval()' to format strings including the use of built-in python source code
                + TODO: Identify alternatives for customizable prompts
            + Implemented CLI argument parsing supported
            + Added optional arguments for customizing the root filesystem mount point and root directory using CLI arguments
    - Additions
        - Added new directory 'core' in 'src/pychroot/' for containing modules/libraries related to the chroot core functionalities
            - Added new directory 'chroot/' for module/libraries involving chroot functions
                - Added new directory 'linux/' for Linux-specific functionalities
                    + Added new module 'chroot.py'
                - Added new directory 'windows/' for Windows-specific functionalities
                    + Added new module 'chroot.py'
        - Added new directory 'utils' in 'src/pychroot' for generic utilities that will be used by the package
            - Added new module/library directory 'io/' containing modules/libraries related to Input/Output (IO) Processing and Handling operations
                + Added new module 'files.py' related to File-related I/O Processing and Handling
            - Added new module/library directory 'system/' containing modules/libraries related to the Operating System/Platform
                + Added new module 'platform.py' : Wrapper/helper library that is built on top of the 'platform' module
    - Bug Fixes

- New
    + Added new document 'FEATURES.md' for all Features in the pipelines
    - Added new directory 'core' in 'src/pychroot/' for containing modules/libraries related to the chroot core functionalities
        - Added new directory 'chroot/' for module/libraries involving chroot functions
            - Added new directory 'linux/' for Linux-specific functionalities
                + Added new module 'chroot.py'
            - Added new directory 'windows/' for Windows-specific functionalities
                + Added new module 'chroot.py'
    - Added new directory 'utils' in 'src/pychroot' for generic utilities that will be used by the package
        - Added new module/library directory 'io/' containing modules/libraries related to Input/Output (IO) Processing and Handling operations
            + Added new module 'files.py' related to File-related I/O Processing and Handling
        - Added new module/library directory 'system/' containing modules/libraries related to the Operating System/Platform
            + Added new module 'platform.py' : Wrapper/helper library that is built on top of the 'platform' module
    - Added new directory 'resources' for project resources and files
        - Added new directory 'demo' for project demo files
            - Added new directory 'gifs' for project demo animation GIFs
                + Added new GIF animation 'pychroot.gif'

- Updates
    - Updated document 'README.md'
        + Added motivation and project information
        + Updated parameters and options
        + Updated package version to 'v0.2.0'
        + Added demo animation GIF
    - Updated the python package configuration file 'pyproject.toml'
        + Updated package version to 'v0.2.0'
    - Updated entry point source code for the REPL 'main.py' in 'src/pychroot/repl/'
        + Refactor: Created new functions and refactored to make the code cleaner
        + Separated functions to related modules for customizability and modularity
        + Added platform checking for cross-platform compatibility
        + Added baseline for command history
        + Added data validation: Null Value check
        + Added PROMPT customization (WIP)
        + REPL/shell infrastructure working
        - Implemented customizable REPL/shell prompt using 'eval()' to format strings including the use of built-in python source code
            + TODO: Identify alternatives for customizable prompts
        + Implemented CLI argument parsing supported
        + Added optional arguments for customizing the root filesystem mount point and root directory using CLI arguments

