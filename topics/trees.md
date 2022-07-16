# Trees

[Back to Welcome page](/welcome.md)

Binary search trees are akin to linked lists in python in that each item in the tree is linked to another item in the tree. These types of relationships in the tree are known as parent child relationships. These types of trees allow for indexing within a database to be accomplished at O(log n) time complexity making them a more efficient storage method than a linked list. However, in the event that the tree is a continual line with only right child elements this time complexity does go up to O(n) depending on how long the tree gets. 

![Binary Search Tree diagram](/pictures/binary_tree.jpeg)
## Purposes and usage
A BST (Binary Search Tree) specifically is made to do what it's name entails. To search itself for the presence of a specific value. It can do this very quickly because of it's structure being a primary parent node being either less than or greater than all following child nodes. Subsequently, each node following is divided in similar fashion. Right Child being reserved for a higher value, left for the lesser value. 

![Binary Search Tree example](/pictures/bst-vs-not-bst.webp)

In the above picture we can see that one important factor of the BST is that all sub trees must abide by the same rules that trees have. Being that a right child node must be greater than the sub tree root. If there are values connected to that sub tree root at the right child position that are greater than the root, this is invalid. 

## [Tree Example](/py%20files/tree.py)




## Problem: 

This is a simple test to see if you understand the basic structure of how a FIFO type queue works. 

Solution is included in the file

[Problem File](/py%20files/queueproblem.py)


## Operations used with Trees

insertion(value): Used to insert new node into the tree or if the tree hasn't been built at all, to establish a root node. O(log n) time complexity

```
def insert(node, key):

    if node is None:
        return Node(key)

    # Adds new node to the left or right child depending on if it is greater or 
    # less than the key given. 
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node
```
deletion(value): Deletes value from the tree. O(log n) time complexity. 

```  
    def deleteNode(self, data,root):

        if self is None:
            return None

        if data < self.data:
            self.leftChild = self.leftChild.deleteNode(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.deleteNode(data,root)
        else:

            # if the node has only one child or no children

            if self.leftChild is None:

                if self == root:
                    temp = self.lowValNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.deleteNode(temp.data,root)

                temp = self.rightChild
                self = None
                return temp
            
            elif self.rightChild is None:

                if self == root:
                    temp = self.highValNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.deleteNode(temp.data,root)

                temp = self.leftChild
                self = None
                return temp

            #if the node has both left and right children,
            # place the next in line value into the position of the deleted node    

            temp = self.lowValNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.deleteNode(temp.data,root)

        return self
```
Search(): Searches for a specific value through the tree and returns the value. This has a O(log n) time complexity as well. 

```
#this explains the type of structure your function would need to have to search properly.

#if searching for the root value:
If root == NULL 
    return NULL;

If number == root->data 
    return root->data;
If number < root->data 
    return search(root->left)
If number > root->data 
    return search(root->right)
```






## References
[BST Tutorial on Programiz.com helped with images](https://www.programiz.com/dsa/binary-search-tree)


## [Back to Welcome page](/welcome.md)
