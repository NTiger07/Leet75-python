rooms1 = [[1], [2], [3], []]
rooms = [
    [1, 3],
    [3, 0, 1],
    [2],
    [0]
]


def canVisitAllRooms(rooms):
    visited = set()

    def explore(room):
        visited.add(room)

        for key in rooms[room]:
            if key not in visited:
                explore(key)

    explore(0)
    return len(visited) == len(rooms)


print(canVisitAllRooms(rooms1))
