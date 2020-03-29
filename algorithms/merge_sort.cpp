#include <iostream>

// Merge sort, also counts number of inversions during sorting.
long sort(int *arr, int len);
long merge_sort(int *arr, int *scratch, int begin, int end);

long sort(int *arr, int len) {
  int *scratch = new int[len / 2 + 1];
  return merge_sort(arr, scratch, 0, len);
}

long merge_sort(int *arr, int *scratch, int begin, int end) {
  if (begin >= end - 128) {
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
  long inversions = merge_sort(arr, scratch, begin, midwayPoint);
  inversions += merge_sort(arr, scratch, midwayPoint, end);

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

int main() {
  int arr[] = {1, 2, 3, 4, 6, 5};
  int len = 6;
  int inversions = sort(arr, len);
  for (int i = 0; i < len; i++) {
    std::cout << arr[i] << ' ';
  }
  std::cout << std::endl;
  std::cout << inversions << std::endl;
  throw 1;
}
