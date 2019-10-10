'''
    Contains utility functions which are commonly needed
'''
import subprocess


def perform_sys_call(cmd):
    returned_val = subprocess.check_output(cmd, shell=True)
    returned_val = returned_val.decode('utf-8')
    return returned_val

print(f"{perform_sys_call('date')}")