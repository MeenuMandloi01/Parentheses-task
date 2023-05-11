class Tree:
    pass

class Leaf(Tree):
    pass

class Branch(Tree):
    def _init_(self, left, right):
        self.left = left
        self.right = right

def treeToParens(tree):
    if isinstance(tree, Leaf):
        return "()"
    else:
        return f"({treeToParens(tree.left)}{treeToParens(tree.right)})"

def parensToTree(str):
    stack = []
    for c in str:
        if c == "(":
            stack.append(None)
        elif c == ")":
            if len(stack) < 2:
                raise ValueError("Invalid input: too many closing parentheses")
            right = stack.pop()
            left = stack.pop()
            stack.append(Branch(left, right))
        else:
            raise ValueError("Invalid input: non-parenthesis character")
        
        if len(stack) != 1:
            raise ValueError("Invalid input: too many opening parentheses")
        return stack.pop()


tree = Branch(Branch(Leaf(), Leaf()), Leaf())
parens = "(()(((((((()))))))))"
treeToParens(tree) == parens
parensToTree(parens) == tree
