// �Ʒ� ������ ���̺귯�� ���
#include <bits/stdc++.h>
using namespace std;

int main(void) {
	// �Ʒ� ������ �Է� ����ȭ
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