# pychroot - Chroot implementation in python with TUI/REPL

## Information
### Project
+ Project Name: py-chroot
+ Package Version: v0.1.0
- Repository:
    + GitHub: https://github.com/Thanatisia/py-chroot

### Description
+ A simple chroot CLI utility made in python that starts up a REPL for traversing the chroot

### Motivation
- I wanted to see if I could make a proper chroot interface/shell in Python as I knew how to do the fundamental workflow on their own (i.e. individual functions to chroot into the system, print and exit)
    + The thought of making a cross-platform chroot utility came to mind, hence the project idea
    + The more I wrote, I somehow ended up with a REPL and I guess a working (albeit incredibly lackluster) shell

## Setup
### Dependencies
+ python
### Pre-Requisites

## Documentations
### Synopsis/Syntax
```bash
py-chroot {options} <arguments>
```

### Parameters
#### Positionals
#### Optionals
- With Arguments
    - `-p | --prompt [custom-prompt]` : Specify the custom string you wish to set as your REPL/shell prompt
        + Type: String
        - Notes
            + Ensure that you wrap your string with a single quote ('your-string') to ensure that none of the string gets executed on boot time
        + Format: `-p '"your-string"'
    - `-r | --root [root-directory]` : Specify the target root directory within the root filesystem to jump into
        + Type: String
    - `-m | --mount [rootfs-mount-path]` : Specify the target root filesystem mount path to chroot into
        + Type: String
- Flags
    + -h | --help
    + -v | --version

### Usage
- Basic Chroot into a new root filesystem
    ```bash
    py-chroot {-m|--mount [rootfs-mount-directory]} {-r|--root [root-directory]}
    ```

### Terminal UI (REPL) Key Commands
- `cd [directory]` : Change directory into the specified directory path
- enter : Enter/Chroot into the specified new rootfs directory
- exit | quit : Exit the REPL shell
- exit-chroot : Exit the current chroot session to go back up to the original rootfs
- help : Display help menu (this)
- version : Display system information
- <default> : The command will be executed on run

## Wiki

## Resources

## References
+ [nessy.info - 2013-12-05 - Python chroot and exit chroot](https://nessy.info/post/2013-12-05-python-chroot-and-exit-chroot/)

## Remarks

