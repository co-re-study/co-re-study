// 기업이 차지할 수 있는 최대 방의 개수는 2개
// 루트 노드까지의 거리가 홀수인 개수와 짝수인 개수 세기

import java.io.*;
import java.util.*;

public class 윤성운 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<List<Integer>> children = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            children.add(new ArrayList<>());
        }
    
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i = 1; i < N; i++) {
            int num = Integer.parseInt(st.nextToken()) - 1;
            children.get(num).add(i);
        }

        Stack<List<Integer>> stack = new Stack<>();
        stack.add(Arrays.asList(0, 0));
        int oddCnt = 0;
        int evenCnt = 0;

        while(!stack.isEmpty()) {
            List<Integer> current = stack.pop();
            if(current.get(1) % 2 == 0) {
                evenCnt++;
            } else {
                oddCnt++;
            }
            for(Integer child : children.get(current.get(0))) {
                stack.add(Arrays.asList(child, current.get(1) + 1));
            }
        }

        System.out.println(Math.min(oddCnt, evenCnt) + Math.abs(oddCnt - evenCnt));
        
    }
}