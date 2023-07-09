// 아래 두줄은 라이브러리 사용
#include <bits/stdc++.h>
using namespace std;

int main(void) {
	// 아래 두줄은 입력 최적화
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	string s;
	cin >> n >> s;
	int day = 0, cnt = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == '(')
			cnt++;
		else
			cnt--;
		if (abs(cnt) > day)
			day = abs(cnt);
	}

	if (cnt == 0)
		cout << day;
	else
		cout << -1;

	return 0;
}