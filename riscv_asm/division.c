
int main(void)
{
    int result = 0;
    int a = 100;
    int b = 34;

    while (a-b >= 0)
    {
        a -= b;
        result++;
    }
    
    
    return result;
}