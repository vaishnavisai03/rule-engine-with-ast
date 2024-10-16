import re

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" or "operand"
        self.value = value     # Condition string (for operands) or operator ('AND', 'OR')
        self.left = left       # Left child (Node)
        self.right = right     # Right child (Node)

    def __repr__(self):
        if self.type == "operand":
            return f"Operand({self.value})"
        else:
            return f"Operator({self.value}) with Left({self.left}) and Right({self.right})"

def parse_rule(rule_string):
    tokens = re.findall(r"[\w']+|[()><=]", rule_string)  # Tokenize the string
    return build_ast(tokens)

def build_ast(tokens):
    if not tokens:
        return None

    # Base condition (operands)
    if len(tokens) == 1:
        return Node(node_type="operand", value=tokens[0])

    # Recursive condition (operators)
    left_token = tokens[0]
    operator = tokens[1]  # AND or OR
    right_token = tokens[2]
    
    left_node = Node(node_type="operand", value=left_token)
    right_node = Node(node_type="operand", value=right_token)

    return Node(node_type="operator", value=operator, left=left_node, right=right_node)
