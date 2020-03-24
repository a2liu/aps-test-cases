// Uses size-based ranks. Only optimization not applied is indexing by 1 to avoid
// set creation requiring two iterations over the array.
public class DisjoinSet {

  static int[] newSet(int setCount) {
    int[] array = new int[setCount];
    for (int i = 0; i < setCount; i ++) {
      array[i] = -1;
    }
    return array;
  }

  static int unionFind(int[] set, int value) {
    if (set[value] < 0) {
      return value;
    } else {
      int root = unionFind(set[value]);
      set[value] = root;
      return root;
    }
  }

  static int mergeSets(int[] set, int l, int r) {
    // Find the root of both of the sets
    int lRoot = unionFind(set, l), rRoot = unionFind(set, r);

    if (lRoot == rRoot) // If they're already merged, return
      return lRoot;

    int lSize = set[lRoot], rSize = set[rRoot]; // Get the size of the sets
    int finalSize = lSize + rSize;

    if (lSize < rSize) { // remember, these values are negative
      disjointSets[lRoot] = finalSize;
      set[rRoot] = lRoot;
      return lRoot;
    } else {
      disjointSets[rRoot] = finalSize;
      set[lRoot] = rRoot;
      return rRoot;
    }
  }
}
