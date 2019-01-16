"""

This script leads to segfault by sending
SIGSEGV signal to the current process without
any handling
"""
import os

if __name__ == "__main__":
    os.kill(os.getpid(), 11)  # 11 means SIGSEGV
