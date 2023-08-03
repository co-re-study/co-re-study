import java.io.*;
import java.util.*;

public class 윤성운 {

    // 상, 하, 좌, 우
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][][] cctvDirections = {
        {{3}, {2}, {1}, {0}},
        {{2, 3}, {0, 1}, {2, 3}, {0, 1}},
        {{0, 3}, {1, 3}, {1, 2}, {0, 2}},
        {{0, 2, 3}, {0, 1, 3}, {1, 2, 3}, {0, 1, 2}},
        {{0, 1, 2, 3}, {0, 1, 2, 3}, {0, 1, 2, 3}, {0, 1, 2, 3}}
    };
    static int answer = 65;

    
    // 중복순열
    static void perm(int depth, int cctvCnt, int[] selection, int[][] cctvs, int N, int M, int[][] arr, int wallCnt) {

        if (depth == cctvCnt) {
            int sightCnt = 0;
            int[][] visited = new int[N][M];
            for(int i = 0; i < cctvCnt; i++) {
                for(int j = 0; j < cctvDirections[cctvs[i][0]][selection[i]].length; j++) {
                    int nr = cctvs[i][1] + dr[cctvDirections[cctvs[i][0]][selection[i]][j]];
                    int nc = cctvs[i][2] + dc[cctvDirections[cctvs[i][0]][selection[i]][j]];
                    while (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                        if (arr[nr][nc] == 6) {
                            break;
                        } else if (arr[nr][nc] == 0 && visited[nr][nc] == 0) {
                            sightCnt++;
                            visited[nr][nc] = 1;
                        }
                        nr += dr[cctvDirections[cctvs[i][0]][selection[i]][j]];
                        nc += dc[cctvDirections[cctvs[i][0]][selection[i]][j]];
                    }
                }
            }
            answer = Math.min(answer, N * M - sightCnt - cctvCnt - wallCnt);
            return;
        }

        for(int i = 0; i < 4; i++) {
            selection[depth] = i;
            perm(depth + 1, cctvCnt, selection, cctvs, N, M, arr, wallCnt);
        }

    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][M];
        int[][] cctvs = new int[8][3];
        int cctvCnt = 0;
        int wallCnt = 0;
        for(int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            for(int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
                if (arr[i][j] > 0 && arr[i][j] < 6) {
                    cctvs[cctvCnt] = new int[]{arr[i][j] - 1, i, j};
                    cctvCnt++;
                } else if (arr[i][j] == 6) {
                    wallCnt++;
                }
            }
        }

        int[] selection = new int[cctvCnt];
        perm(0, cctvCnt, selection, cctvs, N, M, arr, wallCnt);

        System.out.println(answer);
    }
}