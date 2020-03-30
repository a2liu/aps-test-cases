import java.lang.StringBuilder;

class HashMap {

  static float loadFactor = .7f;
  static int TOMBSTONE = -1;
  static int NULL = -2;

  // Initial capacity must be a power of 2
  static int[] newHashMap(int capacity) {
    int arrayLength = capacity * 2 + 1;
    int[] map = new int[arrayLength];
    for (int i = 1; i < arrayLength; i += 2)
      map[i] = NULL;
    return map;
  }

  static int getIndex(int[] hashMap, int key) {
    int capacity = hashMap.length - 1;
    int index = (Integer.hashCode(key) & (capacity - 1) & ~1) + 1;
    for (int current = hashMap[index]; current != NULL;
         current = hashMap[index]) {
      if (current == key) {
        return index;
      }
      index -= 2;
      if (index < 1) {
        index = capacity - 1;
      }
    }
    return index;
  }

  static int putIndex(int[] hashMap, int key) {
    int capacity = hashMap.length - 1;
    int index = (Integer.hashCode(key) & (capacity - 1) & ~1) + 1;
    for (int current = hashMap[index]; current != NULL;
         current = hashMap[index]) {
      if (current == key || current == TOMBSTONE) {
        return index;
      }
      index -= 2;
      if (index < 1) {
        index = capacity - 1;
      }
    }
    return index;
  }

  static int get(int[] hashMap, int key) {
    if (hashMap[0] == 0)
      return NULL;

    int index = getIndex(hashMap, key);
    if (index == NULL || index == TOMBSTONE) {
      return NULL;
    } else {
      return hashMap[index + 1];
    }
  }

  static void putNoAlloc(int[] hashMap, int key, int value) {
    int index = putIndex(hashMap, key);
    if (hashMap[index] == NULL || hashMap[index] == TOMBSTONE) {
      hashMap[0]++;
    }
    hashMap[index] = key;
    hashMap[index + 1] = value;
  }

  static int remove(int[] hashMap, int key) {
    int index = getIndex(hashMap, key);
    if (hashMap[index] == key) {
      hashMap[index] = TOMBSTONE;
      return hashMap[index + 1];
    } else {
      return NULL;
    }
  }

  static int[] put(int[] hashMap, int key, int value) {

    int length = hashMap[0];
    int capacity = hashMap.length - 1;
    if ((capacity >> 1) * loadFactor <= (float)(length + 1)) {
      int[] old = hashMap;
      int oldCapacity = capacity;
      hashMap = newHashMap(capacity * 2);

      for (int i = 1; i < oldCapacity; i += 2) {
        if (old[i] != NULL && old[i] != TOMBSTONE)
          putNoAlloc(hashMap, old[i], old[i + 1]);
      }
    }

    putNoAlloc(hashMap, key, value);
    return hashMap;
  }

  static String toString(int[] hashMap) {
    StringBuilder s = new StringBuilder();
    int capacity = hashMap.length - 1;
    s.append('{');
    for (int i = 1; i < capacity; i += 2) {
      if (hashMap[i] != NULL && hashMap[i] != TOMBSTONE) {
        s.append(hashMap[i] + ":" + hashMap[i + 1] + ",");
      }
    }
    s.append('}');
    return s.toString();
  }
}

class Main {
  public static void main(String[] args) {
    int[] map = HashMap.newHashMap(2);

    map = HashMap.put(map, 0, 12);
    map = HashMap.put(map, 4, 10);
    map = HashMap.put(map, 2, 11);

    System.out.println(HashMap.get(map, 2));
    System.out.println(HashMap.get(map, 0));
    System.out.println(HashMap.get(map, 4));

    HashMap.remove(map, 4);
    System.out.println(HashMap.toString(map));

    HashMap.remove(map, 0);
    HashMap.remove(map, 2);
    System.out.println(HashMap.toString(map));

    throw new RuntimeException();
  }
}
