"""pro_bar.py"""
import os


def hello():
    """hello World"""
    return "Hello " + os.getenv("username")
