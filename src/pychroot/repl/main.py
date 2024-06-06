"""
REPL TUI Interface for traversing around the chroot virtual environment
"""
import os
import sys
from pychroot.utils.system.platform import get_platform_name, is_windows, is_linux

# Check Operating System
host_platform = get_platform_name()
match get_platform_name():
    case "Windows":
        from pychroot.core.chroot.windows.chroot import prepare_system, chroot_prepare, chroot_enter, chroot_exit
    case "Linux":
        from pychroot.core.chroot.linux.chroot import prepare_system, chroot_prepare, chroot_enter, chroot_exit
    case _:
        # Invalid option
        print("Invalid platform: {}".format(host_platform))
        exit(1)

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

def update_prompt(PROMPT):
    """
    Take in a custom string you wish to set as your REPL/shell prompt, evaluate into a python string and return to the loop
    - Notes
        + Because this uses eval(), this uses python string syntax/formatting, and can accept python code on top of regular string
        + However, Security is paramount and as such, I will be looking for alternatives

    :: Params
    - PROMPT : Specify the custom string you wish to set as your REPL/shell prompt
        + Type: String

    :: Output/Return
    - eval : Return the evaluated/executed string into a python string object to display in the while loop
        + Type: String
    """
    return eval('{}'.format(PROMPT))

def start_repl(PROMPT_TEMPLATE="> ", rootfs_mount_dir=".", root_dir=os.getenv("HOME")):
    """
    Start the REPL/shell and take user input
    """
    # Initialize Variables
    line = ""
    command_history = [] # Command history list for input persistency

    # Prepare system and obtain info
    real_root, orig_dir = prepare_system(host_platform, rootfs_mount_dir, root_dir)
    print("[+] Chroot into root directory '{}' in rootfs mount path '{}' successful.".format(root_dir, rootfs_mount_dir))

    # Perform main REPL program loop
    while (line != "exit") or (line != "quit"):
        # Initialize a new prompt using the unevaluated prompt template string
        PROMPT = update_prompt(PROMPT_TEMPLATE)

        # Print prompt and get user input
        line = input(PROMPT)

        # Split line into a list
        cmd_list = line.split()

        # Data Validation: Null Value Check
        if len(cmd_list) > 0:
            # Insert current line to the front of the command history (front = latest/newest, back = previous/oldest)
            command_history.insert(0, line)

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
                    chroot_enter(host_platform, rootfs_mount_dir, root_dir)
                case "exit" | "quit":
                    exit(0)
                case "exit-chroot":
                    chroot_exit(host_platform, real_root, orig_dir)
                case "help":
                    display_help()
                case "version":
                    display_system_version()
                case _:
                    # Default: command
                    rc:int = os.system(line)
        else:
            print("No commands provided.")

def main():
    # Perform pre-initialization setup
    init()

    # Initialize Variables
    PROMPT = '"{}|{}|> ".format(host_platform, os.getcwd())'

    try:
        # Begin the REPL shell
        start_repl(PROMPT_TEMPLATE=PROMPT, rootfs_mount_dir="/", root_dir="../")
    except PermissionError as perm_err:
        # Permission denied
        print(perm_err)

if __name__ == "__main__":
    main()

