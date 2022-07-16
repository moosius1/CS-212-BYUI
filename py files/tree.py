class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


    #function for adding nodes as children to the tree
    def insert(self, data):

        #if new data already exists it cannot be added again
        if self.data == data:
            return False
        
        #If the new data is less than the root it is placed to the left
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True


        # If the new data is greater than the root data it is placed to the right child
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True



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
    

    # function loops through to find lowest node on the right will be used in other functions.

    def highValNode(self, node):
        current = node

        while(current.rightChild is not None):
            current = current.rightChild
        return current


    # function loops through to find lowest node on the left. Will be used in other functions.
    def lowValNode(self, node):
        current = node

        while(current.leftChild is not None):
            current = current.leftChild
        return current

    def find(self, data):
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    
    '''
    The following section is for the printing and iterating through the tree
    for specific ordering of those values. 
    '''

    def preorder(self):
        #this will output values from the top of tree first,
        #  then to it's lower values (left children first),
        # then to it's higher values (right children),
            if self:
                print(str(self.data), end = ' ')
                if self.leftChild:
                    self.leftChild.preorder()
                if self.rightChild:
                    self.rightChild.preorder()
    
    def inorder(self):
        # this will output the values of the tree in increasing order
            if self:
                if self.leftChild:
                    self.leftChild.inorder()
                print(str(self.data), end = ' ')
                if self.rightChild:
                    self.rightChild.inorder()

    def postorder(self):
        # this will output the values of the tree from the smallest
        # value of the left tree upwards then to the lowest value on 
        # the right tree upwards until the root is reached.
            if self:
                if self.leftChild:
                    self.leftChild.postorder()
                if self.rightChild:
                    self.rightChild.postorder()
                print(str(self.data), end = ' ')


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def delete(self, data):
        if self.root is not None:
            return self.root.deleteNode(data, self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def preorder(self):
        if self.root is not None:
            print()
            print('preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('postorder: ')
            self.root.postorder()

tree = Tree()
tree.insert(50)
tree.insert(40)
tree.insert(45)
tree.insert(23)
tree.insert(20)
tree.insert(27)
tree.insert(65)
tree.insert(75)
tree.insert(72)
tree.insert(90)

tree.inorder()
tree.preorder()
