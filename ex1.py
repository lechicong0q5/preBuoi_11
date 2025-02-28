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
    
    def filter_range(self, node, min_price, max_price, result=None):
        if result is None:
            result = []
        if node:
            if node.price > min_price:
                self.filter_range(node.left, min_price, max_price, result)
            if min_price <= node.price <= max_price:
                result.append({"price": node.price, "name": node.name})
            if node.price < max_price:
                self.filter_range(node.right, min_price, max_price, result)
        return result

# Khởi tạo BST và chèn dữ liệu
tree = BinarySearchTree()
iphones = [
    {"price": 3000, "name": "iphone 12"},
    {"price": 1000, "name": "iphone 10"},
    {"price": 5000, "name": "iphone 14"},
    {"price": 2000, "name": "iphone 11"},
    {"price": 4000, "name": "iphone 13"}
]

for iphone in iphones:
    tree.insert(iphone["price"], iphone["name"])

# In ra danh sách các sản phẩm có giá từ 3000 đến 5000
iphone_list = tree.filter_range(tree.root, 3000, 5000)
print("iphone_list =", iphone_list)
