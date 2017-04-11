#-*- coding: utf-8 -*-
import sys, os

class Tree():
    def __init__(self, path, scale = 0):
        self.path  = path
        self.scale = int(scale)

    def show_tree(self):
        complete_list = (self.get_file_list(self.path, self.path.split('/')[-1]))
        self.show_brance(complete_list)

    def get_file_list(self, path, name):
        list = [name]
        if not os.path.isdir(path):
            return list

        for sub_path in os.listdir(path):
            if sub_path in ['.DS_Store' , '.svn']:
                continue
            list.append(self.get_file_list(path + '/' + sub_path, sub_path))

        return list

    def show_brance(self, arr, scale=0, groups = [0],  end=False):
        if self.scale > 0 and scale > self.scale:
            return

        space = ' '
        if scale == 0:
            space = '└'
        else:
            for i in range(0, scale):
                if i == scale -1:
                    if end == True:
                        space = space + '   └'
                        if scale-1 in groups:
                            groups.remove(scale-1)
                    else:
                        space = space + '   ├'
                else:
                    if i in groups:
                        space = space + '   |'
                    else:
                        space = space + '    '

        for index, x in enumerate(arr):
            if isinstance(x, list):
                if not (scale + 1 in groups):
                    groups.append(scale + 1)

                if index == len(arr)-1:
                     self.show_brance(x, scale+1, groups, True)
                else:
                    self.show_brance(x, scale+1, groups, False)

            elif isinstance(x, str):
                print   space + '── ' + x


def help():
    print """
Usage: Tree [options]
            
    \033[32m-p, --path:\033[0m
        Path to the project that you want tree

    \033[32m-d, --depth:\033[0m
        Depth to the tree

    \033[32m-h, --help:\033[0m
        Prints a help message. 
            """
    exit(0)

if __name__ == '__main__':
    i = -1
    for index, arg in enumerate(sys.argv):
        if arg == 'tree.py':
            i = index
            break
    
    
    commands = sys.argv[i+1:]

    path  = os.getcwd()
    scale = 0
    for index, command in enumerate(commands):
        if command == '-p' or command == '--path':
            if index + 1 < len(commands): 
                path = commands[index + 1]
            else:
                print "\033[31mUsed -p, but no path.\033[0m"
                help()
        elif command == '-d' or command == '--depth':
            if index + 1 < len(commands): 
                scale = commands[index + 1]
            else:
                print "\033[31mUsed -d, but no depth.\033[0m"
                help()
        elif command == '-h' or command == '--help':
            help()
            
        
    tree = Tree(path, scale)
    tree.show_tree()
