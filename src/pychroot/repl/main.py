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
    global argv, argc, sys_exec, sys_vers, argparser

    # Retrieve CLI arguments parsed
    exec = sys.argv[0]
    exec_spl = os.path.split(exec)
    exec_path = exec_spl[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Declare and Initialize global variables
    sys_exec = exec_spl[1]
    sys_vers = "v0.1.0"
    argparser = {
        "positionals" : [],
        "optionals" : {
            "with-arguments" : {},
            "flags" : {}
        }
    }

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

def get_cli_arguments():
    # Check if arguments are provided
    if argc > 0:
        # Initialize Variables
        i = 0
        # Open a while loop and iterate through all the arguments
        while i < argc:
            # Get current argument
            curr_arg = argv[i]

            # Match case conditions
            match curr_arg:
                ## Optionals
                ### With Arguments
                case "-p" | "--prompt":
                    """
                    Set the custom prompt for the REPL/shell
                    """
                    # Get next index
                    next_idx = i+1

                    # Check if next index contains any arguments
                    if next_idx <= (argc-1):
                        # Arguments found
                        next_arg = argv[next_idx]

                        # Data Validation: Null Value Check - Check if next argument is empty
                        if next_arg != "":
                            # Map the argument to the key
                            argparser["optionals"]["with-arguments"]["prompt"] = next_arg

                            # Increment counter to skip the next and go to the following element
                            i += 1
                case "-r" | "--root":
                    """
                    Set the target path to set as the root directory within the new root filesystem
                    """
                    # Get next index
                    next_idx = i+1

                    # Check if next index contains any arguments
                    if next_idx <= (argc-1):
                        # Arguments found
                        next_arg = argv[next_idx]

                        # Data Validation: Null Value Check - Check if next argument is empty
                        if next_arg != "":
                            # Map the argument to the key
                            argparser["optionals"]["with-arguments"]["root-directory"] = next_arg

                            # Increment counter to skip the next and go to the following element
                            i += 1
                case "-m" | "--mount":
                    """ 
                    Set the target root filesystem's mount path
                    """
                    # Get next index
                    next_idx = i+1

                    # Check if next index contains any arguments
                    if next_idx <= (argc-1):
                        # Arguments found
                        next_arg = argv[next_idx]

                        # Data Validation: Null Value Check - Check if next argument is empty
                        if next_arg != "":
                            # Map the argument to the key
                            argparser["optionals"]["with-arguments"]["rootfs-mount-directory"] = next_arg

                            # Increment counter to skip the next and go to the following element
                            i += 1
                ### Flags
                case "-h" | "--help":
                    # Enable flag to Display help message
                    argparser["optionals"]["flags"]["help"] = True
                case "-v" | "--version":
                    # Enable flag to Display system version
                    argparser["optionals"]["flags"]["version"] = True
                case _:
                    # Default argument - positional
                    argparser["positionals"].append(curr_arg)

            # Increment the index counter by 1
            i += 1
    else:
        print("No arguments provided.")
        exit(1)

def main():
    # Perform pre-initialization setup
    init()

    # Initialize Variables
    PROMPT = '"{}|{}|> ".format(host_platform, os.getcwd())'
    rootfs_mount_dir = "/"
    root_dir = "../"

    # Obtain parsed CLI arguments
    get_cli_arguments()
    positionals = argparser["positionals"]
    optionals = argparser["optionals"]
    opt_with_Arguments = optionals["with-arguments"]
    opt_Flags = optionals["flags"]

    # Process parsed CLI arguments
    ## Process optional arguments
    for opt_category, opt_values in optionals.items():
        # Get current optional type and optional dictionary values
        for opt_vals_key, opt_vals_val in opt_values.items():
            # Get current key and current value
            match opt_vals_key:
                case "prompt":
                    ## Set the custom prompt for the REPL/shell
                    PROMPT = opt_vals_val
                case "root-directory":
                    ## Set the target path to set as the root directory within the new root filesystem
                    root_dir = opt_vals_val
                case "rootfs-mount-directory":
                    ## Set the target root filesystem's mount path
                    rootfs_mount_dir = opt_vals_val
                case "help":
                    ## Enable flag to Display help message
                    display_help()
                    exit(0)
                case "version":
                    # Enable flag to Display system version
                    display_system_version()
                    exit(0)
                case opt_vals_key if not (opt_vals_key in list(opt_values.keys())):
                    ## Default:: If current option is not in the list of keys
                    print("Invalid optional provided in category [{}]: {}={}".format(opt_category, opt_vals_key, opt_vals_val))

    try:
        # Begin the REPL shell
        start_repl(PROMPT_TEMPLATE=PROMPT, rootfs_mount_dir=rootfs_mount_dir, root_dir=root_dir)
    except PermissionError as perm_err:
        # Permission denied
        print(perm_err)

if __name__ == "__main__":
    main()

