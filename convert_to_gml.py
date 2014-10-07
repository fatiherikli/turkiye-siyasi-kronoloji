# -*- coding: utf-8 -*-

import csv
import networkx as nx


def string_to_list(value):
    return filter(bool, [(item.split(":")[-1]).strip(" +")
            for item in value.split(",")])


def main():
    graph = nx.MultiDiGraph()
    with open('partiler.csv') as f:
        reader = csv.DictReader(f)
        data = list(reader)
            
        for row in data:
            graph.add_node(row['Abbreviation'],
                           label=row['Abbreviation'],
                           type="Party",
                           political_position=row['PoliticalPosition'])

            for descendant in string_to_list(row['DescendantOf']):
                graph.add_edge(row['Abbreviation'], descendant, label="Descendant Of",
                               weight=20)

            for ancestor in string_to_list(row['AncestorOf']):
                graph.add_edge(row['Abbreviation'], ancestor, label="Ancestor Of",
                               weight=20)

            for leader in string_to_list(row['Leader']):
                graph.add_edge(row['Abbreviation'],
                               leader, label="Leader",
                               weight=10)

            for ideology in string_to_list(row['Ideology']):
                graph.add_node(ideology, type="Ideology")
                graph.add_edge(row['Abbreviation'], ideology, label="Ideology",
                               weight=40)

    nx.write_gml(graph, "data.gml")

if __name__ == "__main__":
    main()
