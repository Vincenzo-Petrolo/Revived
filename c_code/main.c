#include "utility_func.c"
#include "printf.c"
#include "iconics.c"

int main(void) {

    // String to use for printing
    int string[100];

    /**
     * FIBONACCI
    */
    // Testing starts
    int result = fibonacci(10);

    if (result == 55) {
        // Use this for printing the word fibonacci
        FIBONACCI_STR
        printf(string);
        // Prints if it was okay
        print_success();
        // Print the result
        print_result(result);
    }



    // Halt the processor
    halt();
}