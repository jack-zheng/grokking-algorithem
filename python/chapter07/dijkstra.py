graph = {}
graph['start'] = {'a':6, 'b': 2}
graph['a'] = {'fin':1}
graph['b'] = {'a':3, 'fin':5}
graph['fin'] = {}

infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def get_lowest_cost_node(costs):
    '''
    Get the lowest cost node from costs map
    '''
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
    print('Find lowest cost node: %s' % lowest_cost_node)
    return lowest_cost_node


def dijstra():
    '''
    Get the lowest cost path to destination
    '''
    node = get_lowest_cost_node(costs)
    while node :
        neighbors_map = graph[node]
        for neighbor in neighbors_map.keys():
            if costs[neighbor] > costs[node] + neighbors_map[neighbor]:
                costs[neighbor] = costs[node] + neighbors_map[neighbor]
                parents[neighbor] = node
        processed.append(node)
        node = get_lowest_cost_node(costs)


def print_trace(parents):
    routes = ['fin']
    node = parents['fin']
    while node:
        routes.append(node)
        if node == 'start':
            break
        node = parents[node]
    for sub in routes[::-1]:
        print('%s -> ' % sub, end='')

if __name__ == '__main__':
    dijstra()
    print('Cheapest cost: %s' % costs['fin'])
    print_trace(parents)