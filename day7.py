# Reddit solution/learning day for directed graphs
import re
import networkx as nx

with open('./inputs/day7.txt', 'r') as input:
    G = nx.DiGraph()

    for line in input:
        m = re.match(r"(.*) bags contain (.*$)", line)

        if m:
            color = m.group(1)
            remain = m.group(2)

            children = re.findall(r"([\d]+) (.*?) bag", remain)
            if not children:
                continue
            for child in children:
                G.add_edge(color, child[1], count=int(child[0]))


def count_bags_in(root):
    total_bags = 0
    for k, val in G[root].items():
        total_bags += val['count'] * count_bags_in(k) + val['count']
    return total_bags


print(len(nx.ancestors(G, 'shiny gold')))
print(count_bags_in('shiny gold'))
