package goldman;

import java.util.LinkedHashSet;
import java.util.Set;


// Using LinkedHashSet which keeps order of adding element
public class LRUCache {
    private final Set<Integer> cache;
    private final int capacity;

    public LRUCache(int capacity) {
        this.cache = new LinkedHashSet<>();
        this.capacity = capacity;
    }

    public void refer(int key) {
        if (!get(key))
            put(key);
    }

    public boolean get(int key) {
        if (!cache.contains(key)) {
            return false;
        }

        cache.remove(key);
        cache.add(key);
        return true;
    }

    public void put(int key) {
        if (cache.contains(key)) {
            cache.remove(key);
        } else if (cache.size() == capacity) {
            int firstKey = cache.iterator().next();
            cache.remove(firstKey);
        }

        cache.add(key);
    }
}
