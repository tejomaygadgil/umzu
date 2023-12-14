states = [
    "will do",
    "doing",
]

colors = [
    "#0047AB", # Blue
    "#EE4B2B", # Red
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
    states_map = dict()
    nodes = set()
    for i, line in enumerate(raw_text):
        if line:
            if line[0] == "#":
                state = line[1:].strip().lower()
                if state in states:
                    current_state = state
                    states_map[current_state] = []
                else:
                    current_state = None
            else:
                if current_state:
                    node = line.strip()
                    states_map[current_state].append(node)
                    nodes.add(node)

    return states_map, nodes

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

    # Create HTML
    above = ["""
<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="shortcut icon" href="#">
  <title>Wozu</title>
</head>

<body>
  <div id="graph" class="mermaid">
    flowchart LR
    
    """]

    below = ["""
</div>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true });
  </script>
</body>

</html>
    """]

    state_text = []
    for state, nodes in states.items():
        color = state_to_color[state]
        for node in nodes:
            state_text.append(f"style {node} fill:{color}")
            state_text.append(f"style {node} color:#FFFFFF")

    html = "\n".join(above + graph_text + state_text + links_text + below)
    
    # Export
    with open("index.html", "w") as f:
        f.write(html)
