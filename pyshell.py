#!/usr/bin/python3

from cmd import Cmd
import pprint
import sqlite3

# https://docs.python.org/3/library/sqlite3.html
# Setup sqlite3
conn = sqlite3.connect('pyshell.db')

# Setup pretty print
pp = pprint.PrettyPrinter(indent=2, width=80, compact=False)

# This loads the json file in for work sets
import json
with open('./source_points.json') as f:
    src_points = json.load(f)

pp.pprint(src_points)

class PyShellPrompt(Cmd):
    prompt = 'pyshell> '
    intro = "\nWelcome! Type ? to list commands\n"

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_add(self, inp):
        print("adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit

if __name__ == '__main__':
    PyShellPrompt().cmdloop()