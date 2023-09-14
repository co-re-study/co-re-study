import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class 윤성운 {

    static boolean valid(StringBuilder sb) {
        for (int i = 1; i <= sb.length() / 2; i++) {
            if (sb.subSequence(sb.length() - i, sb.length()).equals(sb.subSequence(sb.length() - (i * 2), sb.length() - i))) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<BigInteger> goodSequences = new Stack<>();
        goodSequences.add(BigInteger.ONE);
        BigInteger answer = BigInteger.ONE;

        // DFS
        while (!goodSequences.isEmpty()) {
            BigInteger num = goodSequences.pop();
            StringBuilder sb = new StringBuilder(num.toString());
            if (sb.length() == N) {
                answer = num;
                break;
            }
            for (int i = 3; i > 0; i--) {
                if (sb.toString().charAt(sb.length() - 1) != i + 48) {
                    sb.append(Integer.toString(i));
                    if (valid(sb)) {
                        goodSequences.add(new BigInteger(sb.toString()));
                    }
                    sb.deleteCharAt(sb.length() - 1);
                }
            }
        }
        System.out.println(answer);
    }
}