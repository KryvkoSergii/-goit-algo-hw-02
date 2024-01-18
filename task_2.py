from collections import deque

def main(text):
    container = deque()
    
    for i in text:
        container.append(i)
    
    length = int(len(container) / 2)
    for i in range(length):
        right = container.pop()
        left = container.popleft()
        print(f"{right} {left}")
        if right.lower() == left.lower():
            is_polyndrom = True
        else:
            is_polyndrom = False
            break
    
    if is_polyndrom:
        print(f"is polyndrom")
    else:
        print(f"is not polyndrom")

main("AnnA")