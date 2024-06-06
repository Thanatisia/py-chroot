"""
Library/Module containing File I/O Processing and Handling-related functions and utilities
"""
import os
import sys

def get_path_fd(path="/", flags=os.O_RDONLY, **kwargs):
    """
    Open a file descriptor to the specified path, the flags and the mode and return the file descriptor
    """
    fd = os.open(path, flags, **kwargs)
    return fd

