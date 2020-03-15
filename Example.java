import java.io.*;
import java.util.*;
import java.util.Scanner;

/*
 *
 * Tips:
 * 1. Use TreeSet when you need a min-max heap
 * 2. Use TreeMap when you need a min-max heap with values or an ordered map
 * 3. You can multiply numbers by -1 to turn a Min heap inot a max heap
 */
class Main {

  static int[] disjointSets;

  static int unionFind(int value) {
    return disjointSets[value] < 0
        ? value
        : (disjointSets[value] = unionFind(disjointSets[value]));
  }

  static int mergeSets(int l, int r) {
    int lRoot = unionFind(l), rRoot = unionFind(r);
    if (lRoot == rRoot)
      return lRoot;

    int lSize = disjointSets[lRoot], rSize = disjointSets[rRoot];
    int finalSize = lSize + rSize;

    if (lSize < rSize) {
      disjointSets[lRoot] = finalSize;
      return disjointSets[rRoot] = lRoot;
    } else {
      disjointSets[rRoot] = finalSize;
      return disjointSets[lRoot] = rRoot;
    }
  }

  public static void main(String[] args) {
    Scanner input =
        new Scanner(new BufferedReader(new InputStreamReader(System.in)));
  }
}
