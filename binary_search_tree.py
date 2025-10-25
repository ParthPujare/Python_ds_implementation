class Node:

    def __init__(self, key):
        self.key = key
        self.val = None
        self.parent = None
        self.right = None
        self.left = None

    def __repr__(self):
        return(f"{self.key}, {self.val}")

class BST:

    def __init__(self):
        self.root = None

    ##TC---> O(n):worst case O(1): Average case
    def __contains__(self, key):
        curr = self.root
        while curr is not None:
            if key<curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return True
        return False

    ## TC--> O(n)
    def __iter__(self):
        yield from self._in_order(self.root)

    ## TC--> O(n)
    def __repr__(self):
        return str(list(self._in_order(self.root)))

    ##TC---> O(n):worst case O(1): Average case
    def insert(self, key, val):
        if self.root == None:
            self.root = Node(key)
            self.root.val = val
        else:
            curr = self.root
            while True:
                if key<curr.key:
                    if curr.left is None:
                        newnode = Node(key)
                        newnode.val = val
                        newnode.parent = curr
                        curr.left = newnode
                        break
                    else:
                        curr = curr.left
                elif key > curr.key:
                    if curr.right is None:
                        newnode = Node(key)
                        newnode.val = val 
                        newnode.parent = curr
                        curr.right = newnode
                        break
                    else:
                        curr = curr.right
                else:
                    curr.val = val
                    break

    ##TC---> O(n):worst case O(1): Average case
    def search(self, key):
        curr = self.root
        while True:
            if curr == None or curr.key == key:
                return curr
            else:
                if key < curr.key:
                    if curr.left == None:
                        return None
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        return None
                    else:
                        curr = curr.right
                             
    ##TC---> O(n):worst case O(1): Average case
    def delete(self, key):
        node = self.search(key)

        if node is None:
            raise KeyError("Key does not exist !")
        else:
            self._delete(node)

    ##TC---> O(n)
    def traverse(self, order):
        if order == "inorder":
            yield from self._in_order(self.root)
        elif order == "preorder":
            yield from self._pre_order(self.root)
        elif order == 'postorder':
            yield from self._post_order(self.root)
        else:
            raise ValueError("Invalid order!")

    def _delete(self, node):
        if node.left == node.right == None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.key > node.key:
                    node.parent.left = None
                else:
                    node.parent.right = None
                node.parent = None

        elif node.right is None or node.left is None:
            child = node.left if node.left is not None else node.right
            if node.parent == None:
                child.parent = None
                self.root = child
            else:
                if node.parent.right == node:
                    node.parent.right = child
                else:
                    node.parent.left = child
                child.parent = node.parent

            node.parent = node.left = node.right = None

        else:
            successor = self._successor(node)

            node.key = successor.key
            node.val = successor.val

            self._delete(successor)

    def _successor(self, node):
        if node is None:
            raise ValueError("Node successor does not exist!")
        if node.right is None:
            return None
        else:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

    def _predecessor(self, node):
        if node is None:
            raise ValueError("Node predecessor does not exist!")
        if node.left is None:
            return None
        else:
            curr = node.left
            while curr.right:
                curr = curr.right
            return curr

    def _in_order(self, node):
        if node is not None:
            yield from self._in_order(node.left)
            yield (node.key, node.val)
            yield from self._in_order(node.right)

    def _pre_order(self, node):
        if node is not None:
            yield (node.key, node.val)
            yield from self._pre_order(node.left)
            yield from self._pre_order(node.right)

    def _post_order(self, node):
        if node is not None:
            yield from self._post_order(node.left)
            yield from self._post_order(node.right)
            yield (node.key, node.val)


if __name__ == '__main__':
    bst = BST()

    bst.insert(10, 'A')
    bst.insert(5, 'B')
    bst.insert(9, "C")
    bst.insert(2, 'D')
    bst.insert(22, 'E')
    bst.insert(12, 'F')
    bst.insert(30, 'G')
    bst.insert(11, "H")
    bst.insert(15, 'I')
    bst.insert(30, 'J')
    bst.insert(23, 'K')
    bst.insert(35, 'L')
    bst.insert(100, 'M')

    bst.delete(10)

    for i in bst.traverse("preorder"):
        print(i)
    
    print(bst.search(22))
    print(30 in bst)
    print(300 in bst)