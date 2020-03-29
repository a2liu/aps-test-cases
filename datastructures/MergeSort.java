// Merge sort, also counts number of inversions during sorting.
class MergeSort {

  static int sort(int[] arr) {
    int[] scratch = new int[arr.length];
    return mergeSort(arr, scratch, 0, arr.length);
  }

  static int mergeSort(int[] arr, int[] scratch, int begin, int end) {
    if (begin == end || begin == end - 1) {
      return 0;
    }

    int midwayPoint = (end + begin) / 2;
    int inversions = mergeSort(arr, scratch, begin, midwayPoint);
    inversions += mergeSort(arr, scratch, midwayPoint, end);

    for (int i = begin; i < end; i++) {
      scratch[i] = arr[i];
    }

    // merge
    for (int i = begin, leftIdx = begin, rightIdx = midwayPoint; i < end; i++) {
      if (leftIdx == midwayPoint) {
        arr[i] = scratch[rightIdx++];
        continue;
      }

      if (rightIdx == end) {
        arr[i] = scratch[leftIdx++];
        continue;
      }

      int left = scratch[leftIdx], right = scratch[rightIdx];
      if (right < left) {
        arr[i] = right;
        rightIdx++;
        inversions += midwayPoint - leftIdx;
      } else {
        arr[i] = left;
        leftIdx++;
      }
    }
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
