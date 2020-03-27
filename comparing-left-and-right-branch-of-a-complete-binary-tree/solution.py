def solution(arr =[]):
    ret = ""
    if arr is None or len(arr) == 0:
        return ret
    def sum(idx):
        parent = idx - 1
        left = idx * 2
        right = idx * 2 + 1
        if parent < len(arr):
            if parent == -1:
                return 0
            return parent + sum(left) + sum(right)
        return 0
    left = sum(2)
    right = sum(3)
    if left > right:
        ret = "Left"
    elif right > left:
        ret = "Right"
    return ret       

if __name__ == "__main__":
    input = [3, 6, 2, 9, -1, 10]
    print(solution(input))