# @Time : 2020/10/9 15:41
# @Author : LiuBin
# @File : utils.py
# @Description : 
# @Software: PyCharm

import networkx as nx


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        q = [self]
        ret = []
        while q:
            cur = q.pop(0)
            if cur is not None:
                ret.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                ret.append(None)
        while ret[-1] is None:
            ret.pop()
        return repr(ret)


def createList(nodes):
    if not nodes:
        return None
    node = ListNode(nodes[0])
    node.next = createList(nodes[1:])
    return node


def createBiTree(nodes):
    root = None
    queue = []
    flag = True
    for node in nodes:
        if root is None:
            root = TreeNode(node)
            queue.append(root)
        else:
            if flag:
                parent = queue[0]
                if node is not None:
                    parent.left = TreeNode(node)
                    queue.append(parent.left)
            else:
                parent = queue.pop(0)
                if node is not None:
                    parent.right = TreeNode(node)
                    queue.append(parent.right)
            flag = not flag
    return root


if __name__ == '__main__':
    pass
