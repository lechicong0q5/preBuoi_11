import json

class TreeNode:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, price, name):
        if not self.root:
            self.root = TreeNode(price, name)
        else:
            self._insert(self.root, price, name)

    def _insert(self, node, price, name):
        if price < node.price:
            if node.left is None:
                node.left = TreeNode(price, name)
            else:
                self._insert(node.left, price, name)
        else:
            if node.right is None:
                node.right = TreeNode(price, name)
            else:
                self._insert(node.right, price, name)

    def to_dict(self, node):
        if node is None:
            return {}
        return {
            "key": {"price": node.price, "name": node.name},
            "left": self.to_dict(node.left),
            "right": self.to_dict(node.right)
        }

    def print_tree(self):
        tree_dict = self.to_dict(self.root)
        print(json.dumps(tree_dict, indent=2))

tree = BinarySearchTree()
iphones = [
    {"price": 3000, "name": "iphone12"},
    {"price": 1000, "name": "iphone10"},
    {"price": 5000, "name": "iphone14"},
    {"price": 2000, "name": "iphone11"},
    {"price": 4000, "name": "iphone13"}
]

for iphone in iphones:
    tree.insert(iphone["price"], iphone["name"])


tree.print_tree()
