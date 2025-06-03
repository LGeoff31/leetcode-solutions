class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        from collections import deque

        res = 0
        opened = set()
        keys_seen = set()
        boxes_in_hand = set(initialBoxes)
        queue = deque(initialBoxes)

        while queue:
            node = queue.popleft()
            if node in opened:
                continue

            # Can open box if it's open OR you have its key
            if status[node] == 1 or node in keys_seen:
                opened.add(node)
                res += candies[node]
                # Add all new boxes you find
                for x in containedBoxes[node]:
                    if x not in boxes_in_hand:
                        queue.append(x)
                        boxes_in_hand.add(x)
                # Add all new keys you find
                for x in keys[node]:
                    if x not in keys_seen:
                        keys_seen.add(x)
                        # If you just got the key for a box you already have, queue it!
                        if x in boxes_in_hand and x not in opened:
                            queue.append(x)
            else:
                # Can't open now, but still keep in boxes_in_hand
                # Don't lose the box; maybe you'll get a key later
                boxes_in_hand.add(node)
                # Don't append back to queue here; we'll reprocess all unopened boxes after new key/box is found

            # MAIN CHANGE: After processing current queue, if it's empty but there are still boxes_in_hand not opened,
            # and you now have their key, add them to queue to reprocess.
            if not queue:
                # Try any boxes in hand that haven't been opened yet
                for b in list(boxes_in_hand):
                    if b not in opened and (status[b] == 1 or b in keys_seen):
                        queue.append(b)
        return res
