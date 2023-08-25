#include <bits/stdc++.h>
#define MAX 5000001
using namespace std;

int n, m;
vector<pair<int, int>> graph[501]; // {인접노드, 비용}
long long dist[501];

bool bellman_ford(int start)
{
    fill(dist, dist + 501, MAX); // 모든 거리를 무한대로 초기화
    dist[start] = 0;

    for (int i = 1; i <= n; ++i)
    { // 전체를 N번 반복
        for (int j = 1; j <= n; ++j)
        {
            for (auto &edge : graph[j])
            {
                int next_node = edge.first;
                int cost = edge.second;
                if (dist[j] != MAX && dist[next_node] > dist[j] + cost)
                {
                    dist[next_node] = dist[j] + cost;
                    if (i == n)
                        return true; // N번째 반복에서 값이 갱신되면 음수 사이클 존재
                }
            }
        }
    }
    return false;
}

int main()
{
    cin >> n >> m;

    for (int i = 0; i < m; ++i)
    {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
    }

    if (bellman_ford(1))
    {
        cout << -1;
    }
    else
    {
        for (int i = 2; i <= n; ++i)
        {
            if (dist[i] == MAX)
                cout << -1 << "\n";
            else
                cout << dist[i] << "\n";
        }
    }

    return 0;
}
