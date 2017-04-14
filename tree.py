#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Created by wzxjiang on 16/12/26.
#  Copyright © 2016年 wzxjiang. All rights reserved.
#
#  https://github.com/Wzxhaha/tree
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from sys import argv
from os.path import isdir
from os import listdir, getcwd

class Tree():
    def __init__(self, path, depth, ignore):
        self.path = path
        self.depth = int(depth)
        self.ignore = ignore

    def show_tree(self):
        complete_list = (self.get_file_list(self.path, self.path.split('/')[-1]))
        self.show_brance(complete_list)

    def get_file_list(self, path, dir_name):
        dir_names = [dir_name]
        if not isdir(path):
            return dir_names

        for sub_dir_name in listdir(path):
            if sub_dir_name in self.ignore:
                continue
            dir_names.append(self.get_file_list(path + '/' + sub_dir_name, sub_dir_name))

        return dir_names

    def show_brance(self, dir_names, depth=0, groups=[0], end=False):

        # over depth
        if self.depth > 0 and depth > self.depth:
            return

        space = '└'
        if depth != 0:
            space = " "
            for i in range(0, depth):
                # last depth
                if i == depth-1:
                    if end is True:
                        space = space + '   └'
                        if depth-1 in groups:
                            groups.remove(depth-1)
                    else:
                        space = space + '   ├'

                    continue

                # normal
                if i in groups:
                    space = space + '   |'
                else:
                    space = space + '    '

        for index, name in enumerate(dir_names):
            if isinstance(name, list):
                if (depth + 1) not in groups:
                    groups.append(depth + 1)
                if index == len(dir_names)-1:
                    self.show_brance(name, depth+1, groups, True)
                else:
                    self.show_brance(name, depth+1, groups, False)
            elif isinstance(name, str):
                print space + '── ' + name

def log_usage():
    print """
Usage: Tree [options]
            
    \033[32m-p, --path:\033[0m
        Path to the project that you want tree

    \033[32m-d, --depth:\033[0m
        Depth to the tree

    \033[32m--ignore:\033[0m
        Ignore to the dir in tree

    \033[32m-h, --help:\033[0m
        Prints a help message. 
            """
    exit(0)

def main():
    commands = argv[1:]

    path = getcwd()
    depth = 0
    ignore = ['.DS_Store', '.svn', '.git']

    while len(commands):
        command = commands[0]
        del commands[0]
        if command in ['-h', '--help']:
            log_usage()

        if len(commands) == 0:
            print "\n\033[31m[ERROR] >>\n '%s' is the wrong instruction\033[0m" %(command)
            log_usage()

        if command in ['-p', '--path']:
            path = commands[0]
        elif command in ['-d', '--depth']:
            depth = commands[0]
        elif command in ['--ignore']:
            ignore += commands[0].split(',')
        del commands[0]

    tree = Tree(path, depth, ignore)
    tree.show_tree()


if __name__ == '__main__':
    main()
