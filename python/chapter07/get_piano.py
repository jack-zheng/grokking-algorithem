infinity = float('inf')

graph = {}
graph['sheet'] = {'record':5, 'poster':0}
graph['poster'] = {'bass':30, 'drum':35}
graph['record'] = {'bass':15, 'drum':20}
graph['drum'] = {'piano':10}
graph['bass'] = {'piano':20}
graph['piano'] = {}

costs = {}
costs['record'] = 5
costs['poster'] = 0
costs['drum'] = infinity
costs['bass'] = infinity
costs['piano'] = infinity

parents = {}
parents['record'] = 'sheet'
parents['poster'] = 'sheet'
parents['drum'] = None
parents['bass'] = None
parents['piano'] = None

processed = []

def print_trace(parents):
    routes = ['piano']
    node = parents['piano']
    while node:
        routes.append(node)
        if node == 'sheet':
            break
        node = parents[node]
    for sub in routes[::-1]:
        print('%s -> ' % sub, end='')

def get_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node

def dijstra():
    node = get_lowest_cost_node(costs)
    while node:
        neighbors_map = graph[node]
        for neighbor in neighbors_map.keys():
            if costs[neighbor] > costs[node] + neighbors_map[neighbor]:
                costs[neighbor] = costs[node] + neighbors_map[neighbor]
                parents[neighbor] = node
        processed.append(node)
        node = get_lowest_cost_node(costs)

if __name__ == '__main__':
    dijstra()
    print('Cheapest cost: %s' % costs['piano'])
    print_trace(parents)