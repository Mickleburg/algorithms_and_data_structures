from Tree import TreeNode
from collections import deque


def levelOrder(root: TreeNode):
    if root is None:
        return []
    
    queue = deque([root])
    result = []

    while len(queue) > 0:
        cur_rez = []

        for _ in range(len(queue)):
            node = queue.popleft()
            cur_rez.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        result.append(cur_rez)
    
    return result


def main():
    tree_root = TreeNode.buildTreeIterative([9, 16, 8, 6, 11])

    print(levelOrder(tree_root))


if __name__ == "__main__":
    main()
