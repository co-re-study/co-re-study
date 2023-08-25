#include <bits/stdc++.h>
#define MAX 100001
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); // 버퍼동기화 끄기
    cin.tie(NULL);                    // cout 방출 해제

    int N, Q;
    cin >> N >> Q;
    int pop;
    vector<long long> sum(MAX, 0);
    vector<long long> total(MAX, 0);

    for (int i = 1; i <= N; i++)
    {
        cin >> pop;
        sum[i] = sum[i - 1] + pop;
        total[i] = total[i - 1] + (pop * sum[i - 1]);
    }

    for (int i = 0; i < Q; i++)
    {
        int l, r;
        cin >> l >> r;
        long long fun = total[r] - total[l - 1] - (sum[r] - sum[l - 1]) * sum[l - 1];
        cout << fun << '\n';
    }

    return 0;
}
