def process_graph():
    """
    Read graph.txt and return nodes.
    """
    with open("graph.txt", "r") as f:
        text = f.read().splitlines()

    nodes = set()
    for i, line in enumerate(text):
        if line:
            line_nodes = line.split(' --> ')
            assert len(line_nodes) == 2, f"Malformed: line {i}, '{line}"
            nodes.update(line_nodes)

    return text, nodes


if __name__ == "__main__":
    states = [
        "Want to do",
        "Will do",
        "Doing",
        "Done",
    ]

    colors = [
        "",
        "yellow",
        "red",
        "purple",
    ]

    state_to_color = dict(zip(states, colors))

    color_map = {
        "red": "#EE4B2B",
        "green": "#4CBB17",
        "purple": "#702963",
    }

    # Handle graph.txt
    graph_text, graph_nodes = process_graph()


    print(graph_nodes)
