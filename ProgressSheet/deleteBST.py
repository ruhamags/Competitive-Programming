class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.left = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            
            minNode = self.findMin(root.right)
            root.val = minNode.val
            root.val = self.deleteNode(root.right, minNode.val)
        return root 
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
    