#include <bits/stdc++.h>
#define DIVIDE 1000000000
#define FULLMASK 1023
using namespace std;

int N;
vector<vector<vector<long long>>> dp;

int main()
{
    cin >> N;

    if (N < 10)
    {
        cout << 0 << '\n';
        return 0;
    }

    dp.resize(N + 1, vector<vector<long long>>(10, vector<long long>(1 << 10, 0)));

    // 1자리 숫자 초기화
    for (int i = 1; i <= 9; i++)
    {
        dp[1][i][1 << i] = 1;
    }

    for (int i = 2; i <= N; i++)
    {
        for (int j = 0; j <= 9; j++)
        {
            for (int k = 0; k < 1 << 10; k++)
            {
                if (dp[i - 1][j][k] != 0)
                { // 이전 값이 0이 아닌 경우만 계산
                    if (j == 0)
                    {
                        dp[i][j + 1][k | 1 << (j + 1)] = (dp[i][j + 1][k | 1 << (j + 1)] + dp[i - 1][j][k]) % DIVIDE;
                    }
                    else if (j == 9)
                    {
                        dp[i][j - 1][k | 1 << (j - 1)] = (dp[i][j - 1][k | 1 << (j - 1)] + dp[i - 1][j][k]) % DIVIDE;
                    }
                    else
                    {
                        dp[i][j - 1][k | 1 << (j - 1)] = (dp[i][j - 1][k | 1 << (j - 1)] + dp[i - 1][j][k]) % DIVIDE;
                        dp[i][j + 1][k | 1 << (j + 1)] = (dp[i][j + 1][k | 1 << (j + 1)] + dp[i - 1][j][k]) % DIVIDE;
                    }
                }
            }
        }
    }

    // 디버거
    // for (int i = 1; i <= N; i++)
    // {
    //     for (int j = 0; j <= 9; j++)
    //     {
    //         for (int k = 0; k < (1 << 10); k++)
    //         {
    //             if (dp[i][j][k] != 0)
    //             {
    //                 cout << "dp[" << i << "][" << j << "][" << k << "] = " << dp[i][j][k] << endl;
    //             }
    //         }
    //     }
    // }

    long long result = 0;
    for (int j = 0; j <= 9; j++)
    {
        result = (result + dp[N][j][FULLMASK]) % DIVIDE;
    }
    cout << result << '\n';

    return 0;
}
