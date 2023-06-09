import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class boj_2697 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            System.out.println(solution(input));
        }
    }

    public static String solution(String a) {
        int[] aArray = Arrays.stream(a.split("")).mapToInt(Integer::parseInt).toArray();
        StringBuilder answer = new StringBuilder();
        int start = aArray.length - 1;
        int end = -1;
        int x = -1;
        int y = -1;

        while (start - 1 > end) {
            for (int j = start - 1; j > end; j--) {
                if (aArray[start] > aArray[j]) {
                    if (x > 0 && end == j && aArray[start] > aArray[x]) {
                        y = j;
                        end = j;
                        break;
                    }
                    x = start;
                    y = j;
                    end = j;
                    break;
                }
            }
            start--;
        }

        if (x == -1) {
            return "BIGGEST";
        }

        int temp = aArray[x];
        aArray[x] = aArray[y];
        aArray[y] = temp;

        int[] bArray = Arrays.copyOfRange(aArray, 0, y + 1);
        int[] sortedArray = Arrays.copyOfRange(aArray, y + 1, aArray.length);
        Arrays.sort(sortedArray);

        int[] mergedArray = new int[bArray.length + sortedArray.length];
        System.arraycopy(bArray, 0, mergedArray, 0, bArray.length);
        System.arraycopy(sortedArray, 0, mergedArray, bArray.length, sortedArray.length);

        for (int value : mergedArray) {
            answer.append(value);
        }

        return answer.toString();
    }
}
