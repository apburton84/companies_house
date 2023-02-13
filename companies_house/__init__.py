import requests
import networkx as nx
import matplotlib.pyplot as plt
import http.client as http_client
import logging

from .companies_house import CompaniesHouse
from .company_ownership import CompanyOwnership


def enable_logging():
    """Enable logging for the requests library."""
    file_handler = logging.FileHandler("companies_house_api_request.log")

    file_handler.setLevel(logging.DEBUG)

    logging.getLogger("urllib3").addHandler(file_handler)

    http_client.HTTPConnection.debuglevel = 1


def enable_debugging_request():
    """Enable debugging for the requests library."""
    http_client.HTTPConnection.debuglevel = 1


def disable_debugging_request():
    """Disable debugging for the requests library."""
    http_client.HTTPConnection.debuglevel = 0


def binary_tree_layout(
    G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None
):
    """Position nodes in a binary tree."""
    if pos == None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)

    neighbors = list(G.neighbors(root))

    if parent in neighbors:
        neighbors.remove(parent)

    if len(neighbors) != 0:
        dx = width / 2.0

        leftx = xcenter - dx / 2
        rightx = xcenter + dx / 2

        for neighbor in neighbors:
            if G.nodes[neighbor]["child_status"] == "left":
                pos = binary_tree_layout(
                    G,
                    neighbor,
                    width=dx,
                    vert_gap=vert_gap,
                    vert_loc=vert_loc - vert_gap,
                    xcenter=leftx,
                    pos=pos,
                    parent=root,
                )
            elif G.nodes[neighbor]["child_status"] == "right":
                pos = binary_tree_layout(
                    G,
                    neighbor,
                    width=dx,
                    vert_gap=vert_gap,
                    vert_loc=vert_loc - vert_gap,
                    xcenter=rightx,
                    pos=pos,
                    parent=root,
                )
    return pos


def plot_company_graph(company_number, ownership):
    G = nx.DiGraph()

    for entity in ownership:
        G.add_edge(entity["parent_company"], entity["child_company"])

    for i, node in enumerate(G.nodes()):
        if i % 2 == 0:
            G.nodes[node]["child_status"] = "left"
        else:
            G.nodes[node]["child_status"] = "right"

    fig, ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis("off")

    pos = binary_tree_layout(G, company_number)

    nodes = nx.draw_networkx_nodes(G, pos=pos, ax=ax)
    nx.draw_networkx_edges(G, pos=pos, ax=ax)

    annot = ax.annotate("", xy=(0, 0))

    annot.set_visible(False)

    for node in G.nodes:
        annot.xy = pos[node]
        ax.annotate(f"{node}\n", xy=annot.xy)

    plt.show()
