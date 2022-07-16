''' You are Given the following BST. Is it a valid BST or not? Explain? 
                    10
                 /      \
               5         12
              / \       /   \
            4     8    11    20
                 /          /
                3         15
                         /
                       13  
'''

'''
                    10
                 /      \
               5         12
              / \       /   \
            4     8    11    20
                 /          /
            --->3         15
                         /
                       13  
No it is not a valid BST the 6 as indicated above is misplaced. You cannot have a value from a sub tree
less than that sub tree's root. 
bina



you run the following code 
tree.delete(10)
tree.delete(20)

Please correct any issues found in Problem 1, and show any changes
that would happen after the delete function:
***Note*** not all spaces need to be filled in

                    10
                 /      \
               5         12
              / \       /   \
            4     8    11    20
                 /          /
                3         15
                         /
                       13  


                    12
                 /      \
               5         15
              / \       /   
            4     8    13    
           /                
         3                 
                         
                         

'''

