// Does in-place MSD radix sort; you can provide a min and max value to reduce
// sorting runtime. Could do some of the partitioning right-to-left to reduce
// runtime in the case of negative numbers, but I didn't feel like it.
class RadixSort {

  static void sort(int[] data) {
    sort(data, Integer.MIN_VALUE, Integer.MAX_VALUE);
  }

  static void sort(int[] data, int min, int max) {
    int absoluteValueMask = ~(1 << 31);
    int n = data.length;
    if (min > max) {
      throw new RuntimeException("min is greater than max");
    }

    if (min >= 0 || max < 0) {
      min = min | absoluteValueMask;
      max = min > max ? min : max;

      int i = 30;
      while (i > 0 && (max & (1 << i)) == 0)
        i--;

      radixSort(data, 0, n, i);
    } else {
      int partitionBreak = 0;
      for (int i = 0; i < n; i++) {
        int current = data[i];
        if (current < 0) {
          data[i] = data[partitionBreak];
          data[partitionBreak] = current;
          partitionBreak += 1;
        }
      }

      radixSort(data, 0, partitionBreak, 30);

      int i = 30;
      while (i > 0 && (max & (1 << i)) == 0)
        i--;

      radixSort(data, partitionBreak, n, i);
    }
  }

  // Really should be sort non-negative
  static void radixSort(int[] data, int left, int right, int partitionBit) {
    if (partitionBit < 0 || left >= right) {
      return;
    }

    int partitionBreak = left;
    for (int i = left; i < right; i++) {
      int current = data[i];
      if ((current & (1 << partitionBit)) == 0) {
        data[i] = data[partitionBreak];
        data[partitionBreak] = current;
        partitionBreak += 1;
      }
    }

    radixSort(data, left, partitionBreak, partitionBit - 1);
    radixSort(data, partitionBreak, right, partitionBit - 1);
  }
}

class Main {
  public static void main(String[] args) {

    int[] data = new int[] {-34, 12, 24356, 423, 15, 0, 123, 1, -2};
    RadixSort.sort(data, -34, 24356);

    for (int i : data) {
      System.out.print(i + " ");
    }
    System.out.println();
  }
}
