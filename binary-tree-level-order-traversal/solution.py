from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels

if __name__ == "__main__":
    data = [3,9,20,None,None,15,7]
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            val = next(n)
            if val is not None:
                head.left = TreeNode(val)
                fringe.append(head.left)
            val = next(n)
            if val is not None:
                head.right = TreeNode(val)
                fringe.append(head.right)
        except StopIteration:
            break
    solution = Solution()
    from pprint import pprint
    pprint(solution.levelOrder(tree))
    