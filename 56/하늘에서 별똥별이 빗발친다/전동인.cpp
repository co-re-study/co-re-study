#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, M, L, K;
    cin >> N >> M >> L >> K;

    vector<pair<int, int>> stars(K);
    for (int i = 0; i < K; i++)
    {
        cin >> stars[i].first >> stars[i].second;
    }

    int maxCovered = 0;
    for (int i = 0; i < K; i++)
    {
        for (int j = 0; j < K; j++)
        {
            int x1 = stars[i].first;
            int y1 = stars[j].second;
            int x2 = x1 + L;
            int y2 = y1 + L;

            int covered = 0;
            for (int k = 0; k < K; k++)
            {
                if (stars[k].first >= x1 && stars[k].first <= x2 && stars[k].second >= y1 && stars[k].second <= y2)
                {
                    covered++;
                }
            }
            maxCovered = max(maxCovered, covered);
        }
    }

    cout << K - maxCovered << endl;

    return 0;
}
