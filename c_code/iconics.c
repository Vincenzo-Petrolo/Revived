/**
 * Iconics algorithms in C
*/

// Binary search

int binary_search(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}


// QUICK SORT

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pivot_index = partition(arr, low, high);
        quick_sort(arr, low, pivot_index - 1);
        quick_sort(arr, pivot_index + 1, high);
    }
}


// Recursive fibonacci

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    unsigned int res1 = fibonacci(n-1);
    unsigned int res2 = fibonacci(n-2);
    unsigned int result = res1 + res2;
    return result;
}


// Recursive multiplication
int mul(int a, int b) {
    if (b == 0) {
        return 0;
    }

    return a + mul(a, b-1);
}