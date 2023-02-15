#include "math.c"
/**
 * Iconics algorithms in C
*/

// Binary search

int binary_search(int arr[], int n,  int target) {
    unsigned int low = 0, high = n - 1;
    while ((int)low <= (int)high) {
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

int is_sorted(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return 0;
        }
    }
    return 1;
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

#define C1 2
#define C2 2
#define R1 2
#define R2 2

// Matrix multiplication of 2 2x2 matrices

int mulMat()
{
    // Do Matrix-Matrix Multiplication
    int mat1[R1][C1];
    int mat2[R2][C2];
    int result[R1][C2];

    // Initialize the matrix values
    mat1[0][0] = 1;
    mat1[0][1] = 2;
    mat1[1][0] = 3;
    mat1[1][1] = 4;

    mat2[0][0] = 1;
    mat2[0][1] = 2;
    mat2[1][0] = 3;
    mat2[1][1] = 4;
 
    for (int i = 0; i < R1; i++) {
        for (int j = 0; j < C2; j++) {
            result[i][j] = 0;
 
            for (int k = 0; k < R2; k++) {
                result[i][j] += mul(mat1[i][k],mat2[k][j]);
            }
 
        }
    }

    // Check the result

    if (result[0][0] == 7 && result[0][1] == 10 && result[1][0] == 15 && result[1][1] == 22) {
        return 1;
    }


    return 0;

}