#define DISPLAY_ADDRESS 4100
#define DISPLAY_SIZE 20
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


// Each cell in the string, contains 1 char
// because our memory is word addressable
void printf(int *string)
{
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
    for (int i = 0; i < DISPLAY_SIZE; i++)
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
        unsigned int tmp = result & mask;
        //Get the index
        unsigned int index = tmp >> (i*4);
        // Assign to the buffer
        string[17-i] = lut[index];
    }
    
    printf(string);

    return;
}

void print_success(void) {
    clear_buffer();

    int *buffer = DISPLAY_ADDRESS;
    buffer[0] = 'Y';
    buffer[1] = 'e';
    buffer[2] = 's';

    return;
}
