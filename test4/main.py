class Window:
    def __init__(self, cnt, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cnt = cnt


windows = []
window_count = int(input())

for i in range(window_count):
    cnt, x1, y1, x2, y2 = map(int, input().split())
    windows.append(Window(cnt, x1, y1, x2, y2))

click_count = int(input())

for i in range(click_count):
    x, y = map(int, input().split())
    for window in windows:
        if window.x1 <= x <= window.x2 and window.y1 <= y <= window.y2:
            windows.remove(window)
            windows.insert(0, window)
            break

for window in windows:
    print(window.cnt, end=" ")
