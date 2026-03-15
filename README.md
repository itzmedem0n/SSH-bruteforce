                                                                                                     # SSH-bruteforce

Description

This script attempts to find the correct SSH password for a target machine

by trying passwords from a wordlist using multiple threads.

It uses the Paramiko library to establish SSH connections and tests each

password until the correct one is found or the wordlist is exhausted.

-------------------------------------------------------------------------------------------------
Features

Multithreaded password attempts

Automatic SSH host key acceptance

Stops when the correct password is found

Handles authentication errors and connection errors

-------------------------------------------------------------------------------------------------
Requirements

Python 3/ paramiko library

Install dependency:
pip install paramiko

-------------------------------------------------------------------------------------------------
Usage 

Run the script -> python brutefssh.py

You will be prompted for:

Target host IP

SSH username

Wordlist file path

-------------------------------------------------------------------------------------------------
Exemple

Enter the host(target Machine..) : 192.168.1.10

Enter Username: user

Enter wordlist's path(Ex : .../.../.../) : /usr/share/wordlists/rockyou.txt


