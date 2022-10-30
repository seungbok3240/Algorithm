import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main_4386 {

    static int N;
    static ArrayList<float[]> stars;

    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(bf.readLine());
        stars = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            float a = Float.parseFloat(st.nextToken());
            float b = Float.parseFloat(st.nextToken());

            stars.add(new float[]{a, b});
        }

        PriorityQueue<Point> pq = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(i == j) continue;
                float[] s1 = stars.get(i);
                float[] s2 = stars.get(j);

                float dist = (float) Math.sqrt(Math.pow(Math.abs(s1[0] - s2[0]), 2) + Math.pow(Math.abs(s1[1] - s2[1]), 2));
                pq.offer(new Point(i, j, dist));
            }
        }

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        int vCnt = 0;
        float answer = 0;
        while (!pq.isEmpty()) {
            Point p = pq.poll();
            int y = p.y;
            int x = p.x;
            float dist = p.dist;

            if(find(y) != find(x)) {
                union(y, x);
                vCnt++;
                answer += dist;
                if(vCnt == N - 1) break;
            }
        }

        System.out.printf("%.2f", answer);

    }

    private static void union(int y, int x) {
        int py = find(y);
        int px = find(x);

        if(py <= px) parent[px] = py;
        else parent[py] = px;
    }

    private static int find(int a) {
        if(parent[a] != a) {
            parent[a] = find(parent[a]);
        }
        return parent[a];
    }

    static class Point implements Comparable<Point> {
        int y;
        int x;
        float dist;

        public Point(int y, int x, float dist) {
            this.y = y;
            this.x = x;
            this.dist = dist;
        }

        @Override
        public int compareTo(Point o) {
            return Float.compare(this.dist, o.dist);
        }
    }
}
