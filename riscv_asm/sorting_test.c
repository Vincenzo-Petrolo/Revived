#include "./sortings.c"

#define DATAMEM_SIZE 256

int main(void) {
    int* arr = DATAMEM_SIZE;
    int n = 5;

    arr[0] = 5;
    arr[1] = 4;
    arr[2] = 3;
    arr[3] = 2;
    arr[4] = 1;

    
    bubbleSort(arr, n);
    while(1);

    return 0;
}