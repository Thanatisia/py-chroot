"""
Library/Module containing Systems Programming (i.e. Platform/Operating System information)-related functions and utilities
"""
import os
import sys
import platform

def get_platform_name():
    return platform.system()

def is_windows(host_platform):
    # Initialize Variables
    token = False

    # Check condition
    if host_platform.lower() == "windows": 
        token = True
    else:
        token = False

    return token

def is_linux(host_platform):
    # Initialize Variables
    token = False

    # Check condition
    if host_platform.lower() == "linux": 
        token = True
    else:
        token = False

    return token

