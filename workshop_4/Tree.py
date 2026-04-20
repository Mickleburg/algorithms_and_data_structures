from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def buildTreeIterative(arr):
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            current = queue.popleft()

            if i < len(arr) and arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)

                i += 1

            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)

                i += 1

        return root