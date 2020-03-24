class RadixSort {
  static void sort(int[] data, int min, int max) {
    int n = data.length;
    if (min > max) {
      throw new RuntimeException("min is greater than max");
    }

    if (min >= 0 || max < 0) {
      radixSort(data, 0, n, 30);
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
      radixSort(data, partitionBreak, n, 30);
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

    int[] data = new int[] {12, 24356, 423, 15, 0, -1, -345, 123, -45, 12};
    RadixSort.sort(data, -345, 24356);

    for (int i : data) {
      System.out.print(i + " ");
    }
    System.out.println();

    throw new RuntimeException();
  }
}
