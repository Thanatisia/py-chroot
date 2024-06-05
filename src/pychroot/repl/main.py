"""
REPL TUI Interface for traversing around the chroot virtual environment
"""
import os
import sys

def display_help():
    """
    Display help message
    """
    msg = """
## Documentations
### Synopsis/Syntax

py-chroot <optionals> <arguments>

### Parameters
- Positionals
- Optionals

### Usage
- Initialize shell
    py-chroot

### Terminal UI (REPL) Key Commands
- `cd [directory]` : Change directory into the specified directory path
- enter : Enter/Chroot into the specified new rootfs directory
- exit | quit : Exit the REPL shell
- exit-chroot : Exit the current chroot session to go back up to the original rootfs
- help : Display help menu (this)
- version : Display system information
- <default> : The command will be executed on run
    """
    print(msg)

def display_system_version():
    """
    Display the current system information
    """
    msg = """
System Executable: {}
System Version: {}
    """.format(sys_exec, sys_vers)
    print(msg)

def init():
    global argv, argc, sys_exec, sys_vers

    # Retrieve CLI arguments parsed
    exec = sys.argv[0]
    exec_spl = os.path.split(exec)
    exec_path = exec_spl[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Declare and Initialize global variables
    sys_exec = exec_spl[1]
    sys_vers = "v0.1.0"

def chroot_enter(rootfs_mount_dir, root_dir):
    """
    chroot into the new rootfs directory
    """
    # Change root filesystem
    os.chroot(rootfs_mount_dir)

    # Change root directory
    os.chdir(root_dir)

def main():
    # Perform pre-initialization setup
    init()

    # Initialize Variables
    line = ""
    PROMPT = "> "
    rootfs_mount_dir = "/"
    root_dir = str(os.getenv("HOME"))

    # Get original root filesystem
    real_root = os.open("/", os.O_RDONLY)

    # Get starting working directory
    orig_dir = os.getcwd()

    # Change root filesystem
    os.chroot(rootfs_mount_dir)

    # Change root directory
    os.chdir(root_dir)

    # Perform main REPL program loop
    while (line != "exit") or (line != "quit"):
        # Print prompt and get user input
        line = input(PROMPT)

        # Split line into a list
        cmd_list = line.split()

        # Separate list into command and arguments
        command = cmd_list[0]
        cmd_args = cmd_list[1:]

        # Process line and execute commands
        # NOTE: Some commands like "cd" requires using python functions
        match command.lower():
            case "cd":
                # Change directory
                os.chdir(" ".join(cmd_args))
            case "enter":
                chroot_enter(rootfs_mount_dir, root_dir)
            case "exit" | "quit":
                exit(0)
            case "exit-chroot":
                os.fchdir(real_root)
                os.chroot(".")
                os.chdir(orig_dir)
            case "help":
                display_help()
            case "version":
                display_system_version()
            case _:
                # Default: command
                rc:int = os.system(line)

if __name__ == "__main__":
    main()

