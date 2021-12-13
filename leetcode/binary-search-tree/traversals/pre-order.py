from typing import List

def preorder(root):
    answer = []
    preorder(root, answer)
    return answer

def preorder(root, answer: List):
    if root is None:
        return

    answer.append(root.val)
    preorder(root.left, answer)
    preorder(root.right, answer)