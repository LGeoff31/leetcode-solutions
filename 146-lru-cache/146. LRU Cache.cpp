
class LRUCache {
    int capacity;
    list<int> lru; 
    unordered_map<int, pair<int, list<int>::iterator>> cache;

public:
    LRUCache(int capacity) : capacity(capacity) {}

    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;

        lru.splice(lru.begin(), lru, it->second.second);

        return it->second.first;
    }

    void put(int key, int value) {
        auto it = cache.find(key);

        if (it != cache.end()) {
            lru.splice(lru.begin(), lru, it->second.second);
            it->second.first = value;
            return;
        }

        if (cache.size() == capacity) {
            int keyToDelete = lru.back();
            lru.pop_back();
            cache.erase(keyToDelete);
        }

        lru.push_front(key);
        cache[key] = {value, lru.begin()};
    }
};
