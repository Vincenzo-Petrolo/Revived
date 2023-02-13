#include "utility_func.c"
#include "printf.c"
#include "iconics.c"

int main(void)
{

    // String to use for printing
    int string[100];

    /**
     * FIBONACCI
     */
    // Testing starts
    int result = fibonacci(10);

    if (result == 55)
    {
        // Use this for printing the word fibonacci
        FIBONACCI_STR
        printf(string);
        // Prints if it was okay
        print_success();
        // Print the result
        print_result(result);
    }

    /**
     * Quick sort
     */
    int array[10];
    array[0] = 10;
    array[1] = 9;
    array[2] = 8;
    array[3] = 7;
    array[4] = 6;
    array[5] = 5;
    array[6] = 4;
    array[7] = 3;
    array[8] = 2;
    array[9] = 1;

    // Do quick sort
    quick_sort(array, 0, 9);
    int flag = is_sorted(array, 10);

    if (flag == 1)
    {
        // Use this for printing the word "Quicksort"
        QUICKSORT_STR 
        printf(string);
        // Prints if it was okay
        print_success();
    }

    // Halt the processor
    halt();
}