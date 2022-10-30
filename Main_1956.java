import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1956 {

    public static final int MAX = 4000001;  // max 값 설정 확인 잘하기!!!
    static int V, E;
    static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        arr = new int[V + 1][V + 1];
        for (int i = 1; i < V + 1; i++) {
            Arrays.fill(arr[i], MAX);
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            arr[a][b] = w;
        }

        for (int k = 1; k < V + 1; k++) {
            for (int i = 1; i < V + 1; i++) {
                for (int j = 1; j < V + 1; j++) {
                    arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j]);
                }
            }
        }

        int answer = MAX;
        for (int i = 1; i < V + 1; i++) {
            for (int j = 1; j < V + 1; j++) {
                if (arr[i][j] != MAX && arr[j][i] != MAX) {
                    if(i == j) answer = Math.min(answer, arr[i][j]);
                    else answer = Math.min(answer, arr[i][j] + arr[j][i]);
                }
            }
        }

        System.out.println(answer == MAX ? -1 : answer);
    }
}
