#include <stdio.h>

int route[1000][2];
int value[100000];
int time[100000];



void updateRoute(int start_position, int e)
{
    if(start_position < 0) return;

    int start = route[start_position][0];
    if(start == e)
    {
        int end = route[start_position][1];

        if(value[start-1] + time[end-1] >= value[end-1])
            value[end-1] = value[start-1] + time[end-1];
    }

    updateRoute(start_position - 1, e);
}

int main()
{
    int i, problem_count;
    freopen("1005.txt", "r", stdin);
    scanf("%d", &problem_count);

    for(i=0; i<problem_count; i++)
    {
        int j, k, array_count, rule_count;
        scanf("%d %d", &array_count, &rule_count);
        for(j=0; j<array_count; j++)
        {
            scanf("%d", &value[j]);
            time[j] = value[j];
        }

        for(k=0; k<rule_count; k++)
        {
            int start, end;
            scanf("%d %d", &start, &end);
            route[k][0] = start;
            route[k][1] = end;

            updateRoute(k, end);
        }

        int rtv;
        scanf("%d", &rtv);

        printf("%d\n", value[rtv-1]);
    }
}