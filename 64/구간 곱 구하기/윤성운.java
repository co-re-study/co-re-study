import java.io.*;
import java.util.*;

public class 윤성운 {

    static long makeTree(long[] tree, long[] nums, int left, int right, int node) {
        if(left == right) {
            tree[node] = nums[left];
            return tree[node];
        }
        int middle = (left + right) / 2;
        long leftTree = makeTree(tree, nums, left, middle, node * 2);
        long rightTree = makeTree(tree, nums, middle + 1, right, node * 2 + 1);
        tree[node] = leftTree * rightTree % 1000000007;
        return tree[node];
    }

    static long updateTree(long[] tree, long[] nums, int left, int right, int idx, int node) {
        if(idx < left || idx > right) {
            return tree[node];
        }
        if(left == right) {
            tree[node] = nums[idx];
            return tree[node];
        }
        int middle = (left + right) / 2;
        long leftTree = updateTree(tree, nums, left, middle, idx, node * 2);
        long rightTree = updateTree(tree, nums, middle + 1, right, idx, node * 2 + 1);
        tree[node] = leftTree * rightTree % 1000000007;
        return tree[node];
    }
    
    static long getNum(long[] tree, int left, int right, int start, int end, int node) {
        if(right < start || left > end) {
            return 1;
        }
        if(left >= start && right <= end) {
            return tree[node];
        }
        int middle = (left + right) / 2;
        return getNum(tree, left, middle, start, end, node * 2) 
                * getNum(tree, middle + 1, right, start, end, node * 2 + 1) 
                % 1000000007;
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] nums = new long[n + 1];
        for(int i = 1; i < n + 1; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        long[] tree = new long[n * 4];
        makeTree(tree, nums, 1, n, 1);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i = 0; i < m + k; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            if(st.nextToken().equals("1")) {
                int idx = Integer.parseInt(st.nextToken());
                int num = Integer.parseInt(st.nextToken());
                nums[idx] = num;
                updateTree(tree, nums, 1, n, idx, 1);
            } else {
                long num = getNum(tree, 1, n, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), 1);
                bw.write(num + "\n");
            }
        }
        bw.flush();
        bw.close();
    }    
}
