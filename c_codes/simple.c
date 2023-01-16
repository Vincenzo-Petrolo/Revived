int add(int, int);

int main(void) {
    int a,b,c;

    a = 1;
    b = 2;

    if (a == 1) {
        c = add(1, b);
    }

    c = add(a,b);

    return c;
}

int add(int a, int b) {
    return a + b;
}