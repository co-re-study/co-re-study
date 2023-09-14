import java.io.*;
import java.util.*;

public class 윤성운 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String string = br.readLine();
        String target = br.readLine();

        Set<String> targetSet = new HashSet<>();
        Stack<List<Integer>> stack = new Stack<>();
        for (int i = 0; i < target.length(); i++) {
            targetSet.add(String.valueOf(target.charAt(i)));
        }

        int targetIdx = 0;
        int[] aliveIdxList = new int[string.length()];

        for (int i = 0; i < string.length(); i++) {
            String current = String.valueOf(string.charAt(i));
            if(targetSet.contains(current)) {
                if(String.valueOf(target.charAt(targetIdx)).equals(current)) {
                    stack.add(new ArrayList<>(Arrays.asList(targetIdx, i)));
                    if(targetIdx + 1 == target.length()) {
                        for(int j = 0; j < target.length(); j++) {
                            aliveIdxList[stack.pop().get(1)] = -1;
                        }
                        if(stack.isEmpty()) {
                            targetIdx = 0;
                        } else {
                            targetIdx = stack.peek().get(0) + 1;
                        }
                    } else {
                        targetIdx++;
                    }
                } else if(String.valueOf(target.charAt(0)).equals(current)) {
                    stack.add(new ArrayList<>(Arrays.asList(0, i)));
                    targetIdx = 1;
                } else {
                    stack = new Stack<>();
                    targetIdx = 0;
                }
            } else {
                stack = new Stack<>();
                targetIdx = 0;
            }

        }
        
        // 정답 출력
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < aliveIdxList.length; i++) {
            if(aliveIdxList[i] == 0) {
                sb.append(String.valueOf(string.charAt(i)));
            }
        }
        if(sb.length() == 0) {
            System.out.println("FRULA");
        } else {
            System.out.println(sb.toString());
        }
        
    }
}