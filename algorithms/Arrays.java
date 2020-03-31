import java.lang.Math;

class Arrays {

  interface Comp {
    int compare(int a, int b);
  }

  static int[] randomArray(int size) {
    int[] data = new int[size];
    for (int i = 0; i < size; i++) {
      data[i] = (int)(Math.random() * size);
    }
    return data;
  }

  static void sort(int[] data, Comp comp) {
    quickSort(data, 0, data.length, comp);
  }

  static void quickSort(int[] data, int left, int right, Comp comp) {
    if (left >= right - 16) {
      for (int i = left + 1; i < right; ++i) {
        int key = data[i], j = i;
        for (; j > left && comp.compare(data[j - 1], key) > 0; j--)
          data[j] = data[j - 1];
        data[j] = key;
      }
      return;
    }

    int partitionBreak = left;
    int pivot = data[(int)(Math.random() * (right - left)) + left];
    for (int i = left; i < right; i++) {
      int current = data[i];
      if (comp.compare(current, pivot) < 0) {
        data[i] = data[partitionBreak];
        data[partitionBreak] = current;
        partitionBreak += 1;
      }
    }

    quickSort(data, left, partitionBreak, comp);
    quickSort(data, partitionBreak, right, comp);
  }

  static void sort(int[] data) {
    int partitionBreak = 0, n = data.length;
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

  static void radixSort(int[] data, int left, int right, int partitionBit) {
    if (partitionBit < 0)
      return;
    if (left >= right - 256) { // Insertion sort
      for (int i = left + 1; i < right; ++i) {
        int key = data[i], j = i;
        for (; j > left && data[j - 1] > key; j--)
          data[j] = data[j - 1];
        data[j] = key;
      }
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

  static <T> String toString(T[] array) {
    String[] output = new String[array.length];
    StringBuilder s = new StringBuilder();
    for (int i = 0; i < array.length; i++) {
      output[i] = array[i].toString();
    }

    return String.join(" ", output);
  }

  static String toString(int[] array) {
    String[] output = new String[array.length];
    StringBuilder s = new StringBuilder();
    for (int i = 0; i < array.length; i++) {
      output[i] = Integer.toString(array[i]);
    }

    return String.join(" ", output);
  }
}

class Main {
  public static void main(String[] args) {
    int[] randomArray = Arrays.randomArray(100);
    System.out.println(Arrays.toString(randomArray));
    Arrays.sort(randomArray, (a, b) -> a - b);
    System.out.println(Arrays.toString(randomArray));
    throw new RuntimeException();
  }
}
