import java.io.*;
import java.util.*;
import java.util.Scanner;

/*
 *
 */
class Main {

  static int[] disjointSets;
  static void initSets(int n) {
    for (int i = 0; i < n; i++)
      disjointSets[i] = -1;
  }
  static int unionFind(int value) {
    if (disjointSets[value] < 0)
      return value;
    else
      return disjointSets[value] = unionFind(disjointSets[value]);
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
