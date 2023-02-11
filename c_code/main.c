#include "utility_func.c"
#include "printf.c"
#include "iconics.c"

int main(void) {

    int a = 10;
    int b = 2;
    int result = fibonacci(a);

    print_result(result);

    // Halt the processor
    halt();
}