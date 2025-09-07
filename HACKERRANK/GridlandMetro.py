def gridlandMetro(n, m, k, track):
    from collections import defaultdict

    rows = defaultdict(list)
    for r, c1, c2 in track:
        rows[r].append((c1, c2))
    total_tracks = 0
    for r in rows:
        intervals = sorted(rows[r], key=lambda x: x[0])
        merged = []
        current_start, current_end = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= current_end:   
                current_end = max(current_end, end)
            else:   
                merged.append((current_start, current_end))
                current_start, current_end = start, end
        merged.append((current_start, current_end))
        for start, end in merged:
            total_tracks += (end - start + 1)
    return n * m - total_tracks
