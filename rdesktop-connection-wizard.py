#!/usr/bin/env python3

import sys
import os
import subprocess
import shutil

DEFAULT_KEYBOARD = "en-us"
DEFAULT_FULLSCREEN = True

def get_input(prompt, default=None):
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()

def get_remote_host():
    env_host = os.environ.get('RDESKTOP_REMOTE_HOST')
    if env_host:
        print(f"Using Remote host from environment: {env_host}")
        return env_host
    return get_input("Remote host IP or hostname")

def check_rdesktop():
    if shutil.which("rdesktop") is None:
        print("Error: rdesktop is not installed or not in the system PATH.")
        print("Please install rdesktop and try again.")
        sys.exit(1)

def execute_command(command, fullscreen):
    print(f"\nGenerated rdesktop command:")
    print(command)
    if fullscreen:
        print("\nNote: Fullscreen mode can be toggled at any time using Ctrl-Alt-Enter.")
    print("\nExecuting rdesktop...")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing rdesktop: {e}")
    except KeyboardInterrupt:
        print("\nrdesktop session terminated by user.")

def main():
    print("rdesktop Connection Wizard")
    print("==========================")

    check_rdesktop()

    use_defaults = get_input("Use default settings? (Y/n)", "Y").lower() != 'n'

    if use_defaults:
        keyboard = DEFAULT_KEYBOARD
        fullscreen = DEFAULT_FULLSCREEN
    else:
        keyboard = get_input("Keyboard layout (e.g., en-us, ja)", DEFAULT_KEYBOARD)
        fullscreen = get_input("Use fullscreen mode? (Y/n)", "Y").lower() != 'n'

    user = get_input("Username (include domain if necessary, e.g., DOMAIN\\\\user)")
    host = get_remote_host()

    fullscreen_flag = "-f" if fullscreen else ""

    command = f"rdesktop {fullscreen_flag} -k {keyboard} -u {user} {host}"

    confirm = get_input("Do you want to execute this command now? (Y/n)", "Y").lower() != 'n'
    if confirm:
        execute_command(command, fullscreen)
    else:
        print("\nCommand not executed. You can run it manually later:")
        print(command)
        if fullscreen:
            print("\nNote: Fullscreen mode can be toggled at any time using Ctrl-Alt-Enter.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nWizard cancelled. Goodbye!")
        sys.exit(1)
