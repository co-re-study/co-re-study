#include <iostream>
#include <vector>
#include <set>
using namespace std;

struct Card
{
    string shape, color, bg;
};

bool isSet(const Card &a, const Card &b, const Card &c)
{
    return ((a.shape == b.shape && b.shape == c.shape) || (a.shape != b.shape && a.shape != c.shape && b.shape != c.shape)) &&
           ((a.color == b.color && b.color == c.color) || (a.color != b.color && a.color != c.color && b.color != c.color)) &&
           ((a.bg == b.bg && b.bg == c.bg) || (a.bg != b.bg && a.bg != c.bg && b.bg != c.bg));
}

int main()
{
    vector<Card> cards(9);
    for (int i = 0; i < 9; i++)
    {
        cin >> cards[i].shape >> cards[i].color >> cards[i].bg;
    }

    int n;
    cin >> n;

    int score = 0;
    set<set<int>> calledSets;
    bool gCalled = false;

    for (int i = 0; i < n; i++)
    {
        char action;
        cin >> action;
        if (action == 'H')
        {
            int a, b, c;
            cin >> a >> b >> c;
            a--;
            b--;
            c--;
            if (isSet(cards[a], cards[b], cards[c]))
            {
                set<int> currentSet = {a, b, c};
                if (calledSets.find(currentSet) == calledSets.end())
                {
                    score++;
                    calledSets.insert(currentSet);
                }
                else
                {
                    score--;
                }
            }
            else
            {
                score--;
            }
        }
        else if (action == 'G')
        {
            int possibleSets = 0;
            for (int x = 0; x < 9; x++)
            {
                for (int y = x + 1; y < 9; y++)
                {
                    for (int z = y + 1; z < 9; z++)
                    {
                        if (isSet(cards[x], cards[y], cards[z]) && calledSets.find({x, y, z}) == calledSets.end())
                        {
                            possibleSets++;
                        }
                    }
                }
            }
            if (!possibleSets && !gCalled)
            {
                score += 3;
                gCalled = true;
            }
            else
            {
                score--;
            }
        }
    }

    cout << score << endl;
    return 0;
}
