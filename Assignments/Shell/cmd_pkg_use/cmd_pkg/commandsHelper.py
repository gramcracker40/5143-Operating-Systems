#!/usr/bin/env python
# from cmd_pkg.__init__ import ls, pwd, cat

from cmd_pkg import grep, cat, exit, ls, pwd 

# from Exit import exit
# from History import history

"""
This function iterates over globals.items() and if one of the values is "callable"
meaning it is a function, then I add it to a dictionary called 'invoke'. I also
add the functions '__doc__' string to a help dictionary.

Methods:
    exists (string) : checks if a command exists (dictionary points to the function)
    help (string) : returns the doc string for a function 
"""


class CommandsHelper(object):
    def __init__(self):
        self.invoke = {}
        self.help = {}

        self.invoke["grep"] = grep
        self.invoke["cat"] = cat
        self.invoke["ls"] = ls
        self.invoke["exit"] = exit
        self.invoke["pwd"] = pwd
        

    def exists(self, cmd):
        return cmd in self.invoke

    def runner(self, cmd, *args, **kwargs):
        return self.invoke[cmd](*args, **kwargs)

    def __repr__(self):
        return f"Commands: {self.invoke}"

    # def help(self,cmd):
    #     return self.commands.invoke[cmd].__doc__


if __name__ == "__main__":
    pass
