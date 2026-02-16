class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        # Build sweep events
        for x, y, l in squares:
            x1, x2 = x, x + l
            y1, y2 = y, y + l
            events.append((y1, 1, x1, x2))   # add
            events.append((y2, -1, x1, x2))  # remove
            xs.add(x1)
            xs.add(x2)

        xs = sorted(xs)
        x_index = {x: i for i, x in enumerate(xs)}
        n = len(xs)

        # Segment Tree
        cnt = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if cnt[node] > 0:
                length[node] = xs[r] - xs[l]
            else:
                length[node] = length[node * 2] + length[node * 2 + 1] if l + 1 < r else 0

        def update(node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                cnt[node] += val
            else:
                mid = (l + r) // 2
                update(node * 2, l, mid, ql, qr, val)
                update(node * 2 + 1, mid, r, ql, qr, val)
            push_up(node, l, r)

        # Sort events by y
        events.sort()
        total_area = 0.0
        prev_y = events[0][0]

        # First sweep: compute total union area
        for y, typ, x1, x2 in events:
            dy = y - prev_y
            total_area += length[1] * dy
            update(1, 0, n - 1, x_index[x1], x_index[x2], typ)
            prev_y = y

        half = total_area / 2
        curr_area = 0.0

        # Reset tree
        cnt = [0] * (4 * n)
        length = [0] * (4 * n)
        prev_y = events[0][0]

        # Second sweep: find split y
        for y, typ, x1, x2 in events:
            dy = y - prev_y
            area_chunk = length[1] * dy
            if curr_area + area_chunk >= half:
                return prev_y + (half - curr_area) / length[1]
            curr_area += area_chunk
            update(1, 0, n - 1, x_index[x1], x_index[x2], typ)
            prev_y = y

        return prev_y
