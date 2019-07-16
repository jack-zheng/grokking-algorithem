from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = [] 


def is_seller(name):
    return 'm' in name

def BFS():
    '''
    Steps:
    1. use map to store relation ship
    2. loop with deque

    if there are duplicate element in list, you need to add a search check
    '''
    search_queue = deque()
    search_queue += graph['you']
    searched = ['you']
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_seller(person):
                print('Person: %s is a seller' % person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

if __name__ == '__main__':
    BFS()