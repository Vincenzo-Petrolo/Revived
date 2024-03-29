#define DISPLAY_ADDRESS 4100
#define DISPLAY_SIZE 20
#define END_OF_TEXT 3
#define LUT_INITIALIZATION \
lut[0] = '0'; \
lut[1] = '1'; \
lut[2] = '2'; \
lut[3] = '3'; \
lut[4] = '4'; \
lut[5] = '5'; \
lut[6] = '6'; \
lut[7] = '7'; \
lut[8] = '8'; \
lut[9] = '9'; \
lut[10] = 'A'; \
lut[11] = 'B'; \
lut[12] = 'C'; \
lut[13] = 'D'; \
lut[14] = 'E'; \
lut[15] = 'F';

#define FIBONACCI_STR \
string[0] = 'F';\
string[1] = 'i';\
string[2] = 'b';\
string[3] = 'o';\
string[4] = 'n';\
string[5] = 'a';\
string[6] = 'c';\
string[7] = 'c';\
string[8] = 'i';\
string[9] = END_OF_TEXT; // END OF TEXT CHAR

#define QUICKSORT_STR \
string[0] = 'Q';\
string[1] = 'u';\
string[2] = 'i';\
string[3] = 'c';\
string[4] = 'k';\
string[5] = 's';\
string[6] = 'o';\
string[7] = 'r';\
string[8] = 't';\
string[9] = END_OF_TEXT; // END OF TEXT CHAR

#define BINARY_SEARCH_STR \
string[0] = 'B';\
string[1] = 'i';\
string[2] = 'n';\
string[3] = 'a';\
string[4] = 'r';\
string[5] = 'y';\
string[6] = 'S';\
string[7] = 'e';\
string[8] = 'a';\
string[9] = 'r';\
string[10] = 'c';\
string[11] = 'h';\
string[12] = END_OF_TEXT; // END OF TEXT CHAR

#define MATRIX_MUL_STR \
string[0] = 'M';\
string[1] = 'a';\
string[2] = 't';\
string[3] = 'r';\
string[4] = 'i';\
string[5] = 'x';\
string[6] = 'M';\
string[7] = 'u';\
string[8] = 'l';\
string[9] = 't';\
string[10] = 'i';\
string[11] = 'p';\
string[12] = 'l';\
string[13] = 'i';\
string[14] = 'c';\
string[15] = 'a';\
string[16] = 't';\
string[17] = 'i';\
string[18] = 'o';\
string[19] = 'n';\
string[10] = END_OF_TEXT; // END OF TEXT CHAR

// Each cell in the string, contains 1 char
// because our memory is word addressable
void printf(int *string)
{
    clear_buffer();

    int *buffer = DISPLAY_ADDRESS;
    // Copy the string into the memory buffer
    for (int i = 0; i < DISPLAY_SIZE; i++)
    {
        buffer[i] = string[i];
    }
    

    return;
}

void clear_buffer(void)
{
    int *buffer = DISPLAY_ADDRESS;
    for (int i = DISPLAY_SIZE - 1; i >= 0; i--)
    {
        buffer[i] = 0;
    }
    
    return;
}

// Hardcoded print result
void print_result(int result)
{

    clear_buffer();

    int *lut;

    LUT_INITIALIZATION

    int string[DISPLAY_SIZE];
    string[0] = 'R';
    string[1] = 'e';
    string[2] = 's';
    string[3] = 'u';
    string[4] = 'l';
    string[5] = 't';
    string[6] = ':';
    string[7] = ' ';
    string[8] = '0';
    string[9] = 'x';

    // Convert integer into a string
    for (int i = 0; i < 8; i++)
    {
        unsigned int mask = 0xF;
        unsigned int masked_value;
        masked_value = 0xF << 4*i;
        unsigned int tmp = result & masked_value;
        //Get the index
        unsigned int index = tmp >> (i*4);
        // Assign to the buffer
        string[17-i] = lut[index];
    }

    string[18] = END_OF_TEXT;
    
    printf(string);

    return;
}

void print_success(void) {
    clear_buffer();

    int *buffer = DISPLAY_ADDRESS;
    buffer[0] = 'Y';
    buffer[1] = 'e';
    buffer[2] = 's';
    buffer[3] = END_OF_TEXT;

    return;
}