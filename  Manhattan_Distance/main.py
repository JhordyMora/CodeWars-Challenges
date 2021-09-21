def manhattan_distance(point_a: list, point_b: list) -> int:
    return abs(point_b[1] - point_a[1]) + abs(point_b[0] - point_a[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(manhattan_distance([1,1],[1,1]))
          # 0
    print(manhattan_distance([5,4],[3,2]))
          # 4
    print(manhattan_distance([1,1],[0,3]))
        # 3
