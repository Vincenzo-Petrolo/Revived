int add(int a, int b);
int sub(int a, int b);
int mul(int a, int times);

int main(void) {
    int a, b, c, d, e;
    a = 1;
    b = 2;

    c = add(a, b);
    d = sub(a, b);
    e = mul(a, b);

    return c;
}

int add(int a, int b)
{
    return a + b;
}
int sub(int a, int b)
{
    return a - b;
}
int mul(int a, int times)
{
    int sum = 0;

    for (int i = 0; i < times; i++)
    {
        sum = add(a, sum);
    }

    return sum;
    
}