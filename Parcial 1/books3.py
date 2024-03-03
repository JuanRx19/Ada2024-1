def main():
    while(True):
        try:
            n, m = map(int, input().split())
        except EOFError:
            break

        vessels = list(map(int, input().split()))
        left = max(vessels)
        right = sum(vessels)

        while left < right:
            mid = (left+right) // 2
            if(is_possible(vessels, m, mid)):
                right = mid
            else:
                left = mid + 1
        print(left)

def is_possible(vessels, m, capacity):
    containers = 1
    current = 0
    for vessel in vessels:
        if current + vessel > capacity:
            containers += 1
            current = vessel
        else:
            current += vessel
    
    return containers <= m

main()