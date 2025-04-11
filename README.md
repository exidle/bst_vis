# Binary Search Tree (BST) graph visualizer written in Python using GraphViz library.

## Usage: 
    python3 nth_bst.py <input_file> <node_value>

The graph is given in a file, containing a list of edges in the BST format.
The node value is the value of the node from which the graph is constructed.

## Description:
This utility aim is to visualize a part of a big BST graph or the whole BST tree if that is small enough.

    The **default margins** are 3 nodes to the left, 3 nodes to the right, 1 node to the top and 3 nodes to the bottom.
    They are given in the code with following values:
    ```
        left_margin = 3
        right_margin = 3
        levels_down = 3
        levels_up = 1

    ```

It is recommended to create virtual environment and install graphviz package: `pip install graphviz`.

The result is saved in the `bst.png` file.

## License
License: MIT.

