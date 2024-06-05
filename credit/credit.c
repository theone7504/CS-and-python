#include <cs50.h>
#include <stdio.h>
int main(void)
{
    //prompt for input
    long num = get_long("Number: ");
    long num1 = num;
    long num2 = num;
    long num3 = num;
    long num4 = num;



    //calcultae checksum
    int checksum = 0;
    while(num != 0)
    {
        num /= 10;
        if (2*(num % 10) > 9)
        {
            int c = 2*(num % 10);
            int split_sum = 0;
            while(c != 0)
            {
                split_sum += c % 10;
                c /= 10;
            }
            checksum += split_sum;
        }
        else
        {
            checksum += 2*(num % 10);
        }

        num /= 10;
    }
    int checksum1 = 0;
    while(num1 != 0)
    {
        checksum1 += num1 % 10;
        num1/=10;
    }
    int checksum2 = 0;
    while(num2 != 0)
    {
        num2/=10;
        checksum2 += num2%10;
        num2/=10;

    }
    int normal = checksum1-checksum2;
    int final_checksum = normal + checksum;





    //check for card length and starting digits
    int count = 0;
    do
    {
    num3 /= 10;
    ++count;
    } while (num3 != 0);

    int starting;
    for(int i = 0; i<count - 2; i++)
    {
        num4 /= 10;
    }
    starting  = num4;



    //print AMEX, MASTERCARD, VISA, or INVALID.
    if (final_checksum % 10 != 0)
        printf("INVALID\n");
    else if ((count == 15) && (starting == 34 || starting == 37))
        printf("AMEX\n");
    else if ((starting/10 == 4) && (count == 13 || count == 16))
        printf("VISA\n");
    else if ((count == 16) && (starting == 51 || starting == 52 || starting == 53 || starting == 54 || starting == 55))
        printf("MASTERCARD\n");
    else
        printf("INVALID\n");
}
