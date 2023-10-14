def canVisitAllRooms(rooms):
    visited = set()

    def explore(room):
        visited.add(room)

        for key in rooms[room]:
            if key not in visited:
                explore(key)

    explore(0)
    return len(visited) == len(rooms)

# Runtime 34ms Beats 93.24% of users with Python
# Memory 13.84MB Beats 58.55% of users with Python

