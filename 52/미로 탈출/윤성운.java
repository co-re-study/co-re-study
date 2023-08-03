import java.io.*;
import java.util.*;

public class 윤성운 {

    public static void main(String[] args) throws IOException {

        // Input 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        String[] input = br.readLine().split(" ");
        int[] current = {Integer.parseInt(input[0]) - 1, Integer.parseInt(input[1]) - 1};
        input = br.readLine().split(" ");
        int[] destination = {Integer.parseInt(input[0]) - 1, Integer.parseInt(input[1]) - 1};

        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        // Queue, visited 생성
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{current[0], current[1], 0, 0});
        int[][][] visited = new int[N][M][2];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = new int[] {987654321, 987654321};
            }
        }

        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        // BFS
        while (!queue.isEmpty()) {
            current = queue.remove();
            if (visited[current[0]][current[1]][current[2]] <= current[3]) {
                continue;
            }
            visited[current[0]][current[1]][current[2]] = current[3];
            if (current[0] == destination[0] && current[1] == destination[1]) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nr = current[0] + dr[i];
                int nc = current[1] + dc[i];
                if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                    if (arr[nr][nc] == 0) {
                        if (visited[nr][nc][current[2]] > current[3] + 1) {
                            queue.add(new int[]{nr, nc, current[2], current[3] + 1});
                        }
                        continue;
                    }
                    if (current[2] == 0 && visited[nr][nc][1] > current[3] + 1) {
                        queue.add(new int[]{nr, nc, 1, current[3] + 1});
                    }
                }
            }
        }

        // 정답 출력
        if (Arrays.stream(visited[destination[0]][destination[1]]).min().getAsInt() == 987654321) {
            System.out.println(-1);
        } else {
            System.out.println(Arrays.stream(visited[destination[0]][destination[1]]).min().getAsInt());
        }
    }
}