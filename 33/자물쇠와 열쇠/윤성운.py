# len(key) * 2 + len(lock) 만큼의 행과 열을 갖는 매트릭스 생성
# 위 매트릭스에서 열쇠 이동하면서 자물쇠 홈과 맞는지 체크하기

def solution(key, lock):
    M = len(key)
    N = len(lock)
    answer = False
    
    # 회전
    def rotate(key):
        new_key = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                new_key[i][j] = key[j][M-i-1]
        return new_key
        
    # 열쇠 맞춰보기
    def check(key_bump_positions):
        nonlocal answer
        
        if len(lock_blank_positions) != len(key_bump_positions):
            return
        for position in key_bump_positions:
            if position not in lock_blank_positions or position in lock_bump_positions:
                return
        answer = True
        return
        
    # 자물쇠 홈과 돌기 좌표 저장
    lock_blank_positions = set()
    lock_bump_positions = set()
    for r in range(N):
        for c in range(N):
            if not lock[r][c]:
                lock_blank_positions.add((r, c))
            else:
                lock_bump_positions.add((r, c))
    
    for _ in range(4): 
        for i in range(N + 2 * M):
            for j in range(N + 2 * M):
                
                # 열쇠 이동
                new_key = [[0] * (N + 2 * M) for _ in range(N + 2 * M)]
                key_bump_positions = []
                for r in range(M):
                    for c in range(M):
                        if i + r >= N + 2 * M or j + c >= N + 2 * M:
                            break
                        new_key[i + r][j + c] = key[r][c]
                        
                # 열쇠 돌기 부분 저장
                for r in range(M, N + M):
                    for c in range(M, N + M):
                        if new_key[r][c]:
                            key_bump_positions.append((r - M, c - M))
                            
                # 열쇠와 자물쇠 맞춰보기
                check(key_bump_positions)

        key = rotate(key)
    
    return answer