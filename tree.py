from sys import exit
from time import sleep
from random import seed, randint


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class Tree:
    def __init__(self):
        self.root = None
        self.height = 0
        self.min = None
        self.max = None

    def seek(self, val, current):
        if current:
            if val == current.value:
                return current
            elif val < current.value:
                return self.seek(val, current.left)
            elif val > current.value:
                return self.seek(val, current.right)
        else:
            return None

    def del_val(self, val, current):
        if not current:
            return None
        if val < current.value:
            current.left = self.del_val(val, current.left)
        elif val > current.value:
            current.right = self.del_val(val, current.right)
        else:
            # Current has just one or no children
            if current.left is None:
                save = current.right
                current = None
                return save
            elif current.right is None:
                save = current.left
                current = None
                return save
            # Current has two children
            sucessor = right_tree_min(current.right)
            current.value = sucessor.value
            current.right = self.del_val(sucessor.value, current.right)

        return current


    def right_tree_min(self, current):
        while current.left is not None:
            current = current.left
        return current


    def add_val(self, val):
        if self.root == None:
            # No root node; Empty tree
            new_node = Node(val)
            self.root = new_node
            return
        else:
            # Start search at root node
            current = self.root
            self.add_seek(val, current)

    def add_seek(self, val, current):
        if val == current.value:
            return
        elif val < current.value:
            if current.left == None:
                new_node = Node(val)
                current.left = new_node
                return
            else:
                self.add_seek(val, current.left)
        elif val > current.value:
            if current.right == None:
                new_node = Node(val)
                current.right = new_node
                return
            else:
                self.add_seek(val, current.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.value, end=" ")

    def show(self):
        while True:
            ord = int(input(
                "Select order to print values. \n1. Inorder\n2. Preorder \n3. Postorder\n: "))
            if ord == 1:
                self.inorder(self.root)
                break
            elif ord == 2:
                self.preorder(self.root)
                break
            elif ord == 3:
                self.postorder(self.root)
                break
            print("Invalid input. Enter 1, 2, or 3.")

    def show_details(self):
        print('Tree height is: {}'.format(self.height))
        print('Tree min value is: {}'.format(self.min))
        print('Tree max value is: {}'.format(self.max))
        print('Tree has {} nodes'.format(len(self.nodes)))
        input('Press enter to return.')


if __name__ == "__main__":
    tree = Tree()

    def create_tree():
        min_val = -1
        max_val = -1
        num_nodes = -1
        while True:
            min_val = int(input('Set a minimum node value: '))
            if min_val > 0 and min_val < 1000:
                break
            else:
                print("Invalid value. Must be 1-999")
        while True:
            max_val = int(input("Set a maximum node value: "))
            if max_val > min_val and max_val < 1000:
                break
            else:
                print("Invalid value. Must be {}-999".format(min_val))
        while True:
            num_nodes = int(input("Set a number of nodes for the tree: "))
            if num_nodes <= (max_val - min_val) and num_nodes > 0:
                break
            else:
                print("Invalid value. Must be 1-{}".format(max_val - min_val))

        # Create the tree
        seed(1)
        node_vals = []
        while len(node_vals) < num_nodes:
            r = randint(min_val, max_val)
            if r not in node_vals:
                tree.add_val(r)
                node_vals.append(r)
        print("Tree created sucessfully")
        sleep(2)

    def add_val():
        val = input("Enter a value to add to the tree: ")
        tree.add_val(int(val))

    def del_val():
        val = input("Enter a value to delete from the tree: ")
        tree.del_val(int(val), tree.root)

    def find_val():
        val = input("Enter a value to search for in tree: ")
        found = tree.seek(int(val), tree.root)
        if found:
            print("{} is in the tree".format(val))
        else:
            print("{} is not in the tree".format(val))
        sleep(2)

    def print_tree():
        tree.show()
        print()
        input("Press enter to continue.")

    menu = {
        "1": ("Create a random tree", create_tree),
        "2": ("Add a value to the tree", add_val),
        "3": ("Remove a value from the tree", del_val),
        "4": ("Determine if a value is in the tree", find_val),
        "5": ("Print the tree", print_tree),
        "6": ("Exit", exit)
    }
    while True:
        print("************************************")
        for key in sorted(menu.keys()):
            print(key, ": ", menu[key][0])
        opt = input("Make a selection: ")
        func = menu.get(opt)
        if func:
            func[1]()
        else:
            print("Invalid choice")
            sleep(2)
        print('\n'*10)
