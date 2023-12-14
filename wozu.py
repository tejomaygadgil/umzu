states = [
    "want to do",
    "will do",
    "doing",
    "done",
]

colors = [
    "",
    "#EE4B2B",
    "#4CBB17",
    "#702963",
]

state_to_color = dict(zip(states, colors))

def read_file(file_path):
    """
    Helper file to read a text file.
    """
    with open(file_path, "r") as f:
        text = f.read().splitlines()

    return text

def read_graph():
    """
    Read graph.txt and return nodes.
    """
    text = read_file("graph.txt")

    nodes = set()
    for i, line in enumerate(text):
        if line:
            if line[0] != "#":  # Ignore comments
                line_nodes = [node.strip() for node in line.split(' --> ')]
                assert len(line_nodes) == 2, f"Malformed: line {i}, '{line}"
                nodes.update(line_nodes)

    return text, nodes

def read_state():
    """
    Read todo.txt and return states and nodes.
    """
    raw_text = read_file("todo.txt")

    current_state = None
    states = dict()
    nodes = set()
    for i, line in enumerate(raw_text):
        if line:
            if line[0] == "#":
                current_state = line[1:].strip()
                states[current_state] = []
            else:
                node = line.strip()
                states[current_state].append(node)
                nodes.add(node)

    return states, nodes

def read_links():
    """
    Read links.txt and return states and nodes.
    """
    raw_text = read_file("links.txt")

    current_state = None
    nodes = set()
    text = list()
    for i, line in enumerate(raw_text):
        if line:
            if line[0] != "#":
                assert ': ' in line, f"Malformed link: line {i}, 'f{line}'"
                node, link = [string.strip() for string in line.split(': ')]
                text.append(f'click {node} "{link}"')
                nodes.add(node)

    return text, nodes


if __name__ == "__main__":

    # Read text files
    graph_text, graph_nodes = read_graph()
    states, state_nodes = read_state()
    links_text, links_nodes = read_links()

    # Consolidate nodes
    nodes = sorted(set.union(*[graph_nodes, state_nodes, links_nodes]))

    """
    text = []
    for state, nodes in states.items():
        color = state_to_color[state]
        for node in nodes:
            text.append(f"style {node} fill
    """
