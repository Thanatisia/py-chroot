# pychroot - Chroot implementation in python with TUI/REPL

## Information
### Description
+ A simple chroot CLI utility made in python that starts up a REPL for traversing the chroot

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
- Flags

### Usage
- Basic Chroot
    ```bash
    py-chroot {-r|--root [root-mount-directory]}
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

