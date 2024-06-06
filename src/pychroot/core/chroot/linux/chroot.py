"""
py-chroot core utilities - Linux-specific Chroot functions and utilities
"""
import os
import sys
from pychroot.utils.io.files import get_path_fd

def chroot_prepare(host_platform, path="/"):
    """
    Prepare for the chroot by returning the file descriptor to the original root filesystem and the original working directory
    """
    # Check if platform is Windows or *NIX-based
    match host_platform.lower():
        case "windows":
            real_root = path
            orig_dir = os.getcwd()
        case _:
            # Non-Windows-based (i.e. *NIX)
            # Get the file descriptor to the original root filesystem
            real_root = get_path_fd(path, os.O_RDONLY)

            # Get starting working directory
            orig_dir = os.getcwd()

    return [real_root, orig_dir]

def chroot_exit(host_platform, original_rootfs_fd, original_root_dir):
    """
    Exit the chroot virtual environment and revert back up to the original root filesystem and root directory
    """
    # Check if platform is Windows or *NIX-based
    match host_platform.lower():
        case "windows":
            os.chdir(original_root_dir)
        case _:
            os.fchdir(original_rootfs_fd)
            os.chroot(".")
            os.chdir(original_root_dir)

def chroot_enter(host_platform, rootfs_mount_dir, root_dir):
    """
    chroot into the new rootfs directory
    """
    # Check if platform is Windows or *NIX-based
    match host_platform.lower():
        case "windows":
            # Change root directory
            os.chdir(root_dir)
        case _:
            # Change root filesystem
            os.chroot(rootfs_mount_dir)

            # Change root directory
            os.chdir(root_dir)

def prepare_system(host_platform, rootfs_mount_dir=".", root_dir=os.getenv("HOME")):
    """
    Check if the host is windows or *nix-based and prepare the system for chroot (for linux)/change directories (for windows)
    """
    # Get the file descriptor to the original root filesystem and the starting working directory
    real_root, orig_dir = chroot_prepare(host_platform)

    # Change into the root filesystem and the new root directory
    chroot_enter(host_platform, rootfs_mount_dir, root_dir)

    return [real_root, orig_dir]

