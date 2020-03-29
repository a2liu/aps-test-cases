// Merge sort, also counts number of inversions during sorting.
class MergeSort {
  static long sort(int[] arr) {
    int[] scratch = new int[arr.length / 2 + 1];
    return mergeSort(arr, scratch, 0, arr.length);
  }

  static long mergeSort(int[] arr, int[] scratch, int begin, int end) {
    if (begin >= end - 256) {
      long inversions = 0;
      for (int i = begin + 1; i < end; ++i) {
        int key = arr[i], j = i;

        for (; j > begin && arr[j - 1] > key; j--)
          arr[j] = arr[j - 1];

        arr[j] = key;
        inversions += i - j;
      }

      return inversions;
    }

    int midwayPoint = (end + begin) >> 1;
    long inversions = mergeSort(arr, scratch, begin, midwayPoint);
    inversions += mergeSort(arr, scratch, midwayPoint, end);

    for (int i = begin; i < midwayPoint; i++) {
      scratch[i - begin] = arr[i];
    }

    // merge
    int scratchEnd = midwayPoint - begin;
    int i = begin, leftIdx = 0, rightIdx = midwayPoint;
    for (; leftIdx != scratchEnd && rightIdx != end; i++) {
      int left = scratch[leftIdx], right = arr[rightIdx];
      if (right < left) {
        arr[i] = right;
        rightIdx++;
        inversions += midwayPoint - leftIdx - begin;
      } else {
        arr[i] = left;
        leftIdx++;
      }
    }

    for (; leftIdx != scratchEnd; leftIdx++, i++)
      arr[i] = scratch[leftIdx];
    for (; rightIdx != end; rightIdx++, i++)
      arr[i] = arr[rightIdx];

    return inversions;
  }
}

class Main {
  public static void main(String[] args) {
    int[] arr = new int[] {1, 2, 3, 4, 6, 5};
    int inversions = MergeSort.sort(arr);
    for (int i : arr) {
      System.out.print(i + " ");
    }
    System.out.println();
    System.out.println(inversions);
    throw new RuntimeException();
  }
}
