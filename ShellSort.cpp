//Using ShellSort for sorting an array of numbers

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <math.h>

using namespace std;

int main()
{
    int NumOfElements;

    printf("Please, enter number of array elements:\t");
    scanf("%d", &NumOfElements);

    int arrayOfNum[NumOfElements];
    int step = NumOfElements;
    int valueForSwap;
    int k = log(2 * NumOfElements - 1)/log(3);

    //Setting array elements randomly
    for (int i = 0; i < NumOfElements; i++)
    {
        arrayOfNum[i] = rand() % NumOfElements;
        printf("%d\t", arrayOfNum[i]);
    }

    //Sort array by ShellSort
    while (step > 1)
    {
        step = (pow(3,k) - 1)/2;
        for (int k = step; k < NumOfElements; k++)
            for (int i = k; i >= step; i -= step)
            {
                if (arrayOfNum[i] < arrayOfNum[i - step])
                {
                    valueForSwap = arrayOfNum[i];
                    arrayOfNum[i] = arrayOfNum [i - step];
                    arrayOfNum[i - step] = valueForSwap;
                }
                else
                    break;
            }
        k--;
    }

    printf("\n");

    for (int i = 0; i < NumOfElements; i++)
        printf("%d\t", arrayOfNum[i]);
}
