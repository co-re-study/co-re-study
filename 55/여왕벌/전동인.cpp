#include <bits/stdc++.h>
using namespace std;

int M, N;
vector<int> grid;

void grow()
{
    for (int i = 0; i < N; i++)
    {
        int zcnt, ocnt, tcnt;
        cin >> zcnt >> ocnt >> tcnt;

        for (int j = zcnt; j < zcnt + ocnt; j++)
            grid[j] += 1;
        for (int j = zcnt + ocnt; j < grid.size(); j++)
            grid[j] += 2;
    }
}

int main()
{
    ios_base::sync_with_stdio(false); // 버퍼동기화 끄기
    cin.tie(NULL);                    // cout 방출 해제

    cin >> M >> N;
    grid = vector<int>(2 * M - 1, 1);

    grow();

    for (int i = 0; i < M; i++)
    {
        cout << grid[M - i - 1] << ' ';
        for (int j = 1; j < M; j++)
        {
            cout << grid[M + j - 1] << ' ';
        }
        cout << '\n';
    }
}