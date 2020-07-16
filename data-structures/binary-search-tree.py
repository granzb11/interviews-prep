from typing import List, Any


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        # if root is null, tree is empty. Initializing tree
        if not self.root:
            self.root = Node(val)
            return

        current = self.root
        new_node = Node(val)
        # finding correct location for insert
        while True:
            # if val is smaller than currentent val
            if val < current.val:
                # if currentent node doesn't have a left node assigned
                if not current.left:
                    current.left = new_node
                    new_node.parent = current
                    break
                else:
                    current = current.left
            # if val is bigger than currentent val
            else:
                if not current.right:
                    current.right = new_node
                    new_node.parent = current
                    break
                else:
                    current = current.right

    def find_node(self, val: int) -> Node:
        if not self.root:
            return None
        current = self.root
        while True:
            # we found a match
            if current.val == val:
                return current
            # value is smaller than curr val
            elif val < current.val:
                if current.left:
                    current = current.left
                # node was not found
                else:
                    return None
            # value is bigger than curr val
            elif val > current.val:
                if current.right:
                    current = current.right
                else:
                    return None


    def remove(self, val: int) -> bool:
        node = self.find_node(val)
        if not node:
            return False
        else:
            return self.delete(node)

    def delete(self, node: object) -> bool:
        """

        :type node: object
        """
        return_bool: bool = False
        # node is root
        if not node.parent:
            self.root = None
            return_bool = True
        # setting parent node
        parent_node = node.parent
        # let's check the type of node we have
        # if node is leaf
        if not node.left and not node.right:
            # if node is the left of the parent
            if parent_node.left == node:
                parent_node.left = None
            # if node is the right of the parent
            else:
                parent_node.right = None
            return_bool = True
        # node is full
        elif node.left and node.right:
            child_right_node = self.leftmost(node.right)
            self.delete(child_right_node)
            return_bool = True
        else:
            # right node exists
            if not node.left and node.right:
                child_node = node.right
            # left node exists
            elif node.left and not node.right:
                child_node = node.left

        node.val = child_node.val
        node.right = child_node.right
        node.left = child_node.left
        if child_node.right:
            child_node.right.parent = node
        if child_node.left:
            child_node.left.parent = node
        child_node = None
        return_bool = True

        return return_bool

    def to_array(self) -> list:
        # uses breadth first search
        if not self.root:
            return list()

        queue_list: List[Any] = []
        current = self.root
        queue_list.append(current)
        i = 0
        while current is not None:
            if current.left:
                queue_list.append(current.left)
            elif current.right:
                queue_list.append(current.right)
            current = queue_list[++i]

        return queue_list

