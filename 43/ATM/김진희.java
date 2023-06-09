import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 김진희 {
    public static void main(String[] args) throws IOException{
        // 버퍼리더로 인풋을 받는다
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 문자로 된 숫자를 바로 숫자로 바꿔서 사람 수에 할당
        int people = Integer.parseInt(br.readLine());
        // 시간 리스트(사람 수 길이)를 만들어야하는데
        int[] time = new int[people];
        // 문자열로 들어오니까 일단 받아서
        StringTokenizer st = new StringTokenizer(br.readLine());
//        br.close()
        // 인풋 받은 리스트(문자열)을 숫자로 바꿔서 내 time리스트에 넣어준다.
        for (int i=0;i<people;i++) {
            time[i] = Integer.parseInt(st.nextToken());
        }
        // time리스트 정렬
        Arrays.sort(time);
        /*  앞에 있는 애는
            뒤에 나올 애들만큼 반복해서 들어갈거니까
            한 번에 곱해서 넣어준다.
         */
        int answer = 0;
        for (int i=0;i<people;i++){
            answer += time[i] * (people - i);
        }
        System.out.println(answer);
    }
}