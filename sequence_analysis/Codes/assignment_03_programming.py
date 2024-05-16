class Node:
    def __init__(self):
        self.children = {}  # Dictionary to store children nodes
        self.parent = None  # Reference to parent node
        self.lcp = 0        # Length of the longest common prefix with parent

    def add_child(self, start, end, lcp):
        # Add a child node with the given start and end positions and LCP
        child = Node()
        child.parent = self
        child.lcp = lcp
        self.children[start] = child

    def length(self):
        # Calculate the length of the edge represented by this node
        return self.parent.lcp + len(self.children)


def construct_suffix_tree(pos, lcp):
    n = len(pos)
    root = Node()  # Initialize the root node of the suffix tree
    lcp_prev = 0   # Initialize previous LCP value to 0

    # Initialize active node and active length
    active_node = root
    active_length = 0

    # Iterate over the POS and LCP arrays
    for i in range(n):
        # Update active node and active length based on LCP
        while lcp[i] < lcp_prev:
            active_node = active_node.parent
            lcp_prev = active_node.lcp

        # Add suffix starting at POS[i] to the suffix tree
        remain_length = n - pos[i]
        while remain_length > 0:
            # If active length is 0, start from the current node
            if active_length == 0:
                if pos[i] + active_length not in active_node.children:
                    active_node.add_child(pos[i], n, lcp[i])
                    remain_length -= 1
                else:
                    active_node = active_node.children[pos[i] + active_length]
                    active_length = active_node.length()
            else:
                # Find the next character in the active edge
                next_char = pos[i] + active_length
                edge_length = active_node.children[next_char].length()

                # If the active length is greater than edge length, move to next node
                if active_length >= edge_length:
                    active_node = active_node.children[next_char]
                    active_length -= edge_length
                else:
                    # Split the edge and add new node
                    split_node = Node()
                    active_node.add_child(pos[i], next_char, lcp[i])
                    split_node.add_child(next_char, n, lcp[i])
                    active_node.children[next_char] = split_node
                    remain_length -= 1

        # Update previous LCP value
        lcp_prev = lcp[i]

    return root


# Test the function with provided POS and LCP arrays
pos = [10, 9, 4, 7, 2, 5, 0, 8, 3, 6, 1]
lcp = [-1, 0, 1, 1, 3, 3, 5, 0, 2, 2, 4, -1]

suffix_tree_root = construct_suffix_tree(pos, lcp)

# Example usage of the constructed suffix tree
# You can traverse the tree from the root node (suffix_tree_root)
# and perform operations like searching for substrings, etc.
