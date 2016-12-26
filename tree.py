#-*- coding: utf-8 -*-
import sys, os

class Tree():
    def __init__(self, path):
        self.path = path

    def show_tree(self):
        complete_list = (self.get_file_list(self.path, self.path.split('/')[-1]))
        self.show_brance(complete_list)

    def get_file_list(self, path, name):
        list = [name]
        if not os.path.isdir(path):
            return list

        for sub_path in os.listdir(path):
            if sub_path == '.DS_Store':
                continue
            list.append(self.get_file_list(path + '/' + sub_path, sub_path))

        return list

    def show_brance(self, arr, scale=0, groups = [0],  end=False):
        space = '|'
        if scale == 0:
            space = '├'
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

if __name__ == '__main__':
    path = os.getcwd()

    if (len(sys.argv) > 1):
        path = sys.argv[1]

    tree = Tree(path)
    tree.show_tree()
