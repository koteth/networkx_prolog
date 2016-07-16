import networkx as nx


def to_prolog(G, filename='G.pl'):

    is_directed = G.is_directed()
    nodes = []
    edges = []
    props = []
    for n, data in G.nodes(data=True):
        nodes.append(n)
        for prop, v in data.items():
            props.append(("node", n, prop, v))

    for f, t, data in G.edges(data=True):
        edges.append((f, t))
        for prop, v in data.items():
            props.append(("edge", (f, t), prop, v)) 

    
    rows = []
    for n in nodes:
        row = "is_node('%s')." % n    
        rows.append(row)

    for f, t in edges:
        row = "is_edge('%s', '%s')." % (f, t)
        if not is_directed:
            row = "is_edge('%s', '%s')." % (t, f)  
        rows.append(row)

    for ptype, el, prop, v in props:

        if ptype == 'node':
            row = "node_property('%s', '%s', '%s')." % (prop, el, v)     
        else:
            row = "edge_property('%s', '%s', '%s', %s)." % (prop, el[0], el[1], v)
        if not is_directed:
            row = "edge_property('%s', '%s', '%s', %s)." % (prop, el[1], el[0], v)
        rows.append(row)

    out_file = open(filename, 'w')
    for r in rows:
        out_file.write("%s\n"%r)

    out_file.close()

