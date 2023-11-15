import java.io.*;
import java.util.*;

public class 윤성운 {

    static int binarySearch(List<Integer> arr, int target) {
        int left = 0;
        int right = arr.size() - 1;
        while(left < right) {
            int middle = (left + right) / 2;
            if(arr.get(middle) >= target) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return left;
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        List<Integer> dp = new ArrayList<>();
        dp.add(nums[0]);
        int[] idxArr = new int[n];
        idxArr[0] = 0;
        for(int i = 1; i < n; i++) {
            if(nums[i] > dp.get(dp.size() - 1)) {
                dp.add(nums[i]);
                idxArr[i] = dp.size() - 1;
                continue;
            }
            int idx = binarySearch(dp, nums[i]);
            dp.set(idx, nums[i]);
            idxArr[i] = idx;
        }

        System.out.println(dp.size());
        int[] answer = new int[dp.size()];
        int current = dp.size() - 1;
        for(int i = n - 1; i >= 0; i--) {
            if(idxArr[i] == current) {
                answer[current] = nums[i];
                current--;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < dp.size(); i++) {
            sb.append(answer[i] + " ");
        }
        System.out.println(sb);
    }    
}
