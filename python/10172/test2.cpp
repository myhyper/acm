#include <stdio.h>

int main(void)
{
  int num = 0;
  int a[1000];
  int count = 0;

  scanf("%d", &num);
  for (int i = 0; i < num; i++)
  {
    scanf("%d", &a[i]);
    for (int j = 2; j <= a[i]; j++)
    {
      if (a[i] % j == 0)
      {
        if (a[i] == j)
          count++;
        else
        {
          break;
        }
      }
    }
  }
  printf("%d", count);

  return 0;
}
