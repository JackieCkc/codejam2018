import java.util.*;
import java.io.*;

public class AntStackLarge {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();

        for (int i = 1; i <= t; i++) {
            int n = in.nextInt();

            long[] weights = new long[n];
            for (int j = 0; j < n; j++) {
                weights[j] = in.nextLong();
            }

            int MAX_ANT = 139;

            long[][] mem = new long[n][MAX_ANT + 1];

            for (int x = 0; x < n; x++) {
                for (int y = 0; y <= MAX_ANT; y++) {
                    if (y == 0) {
                        mem[x][y] = 0;
                        continue;
                    }

                    if (x == 0) {
                        mem[x][y] = y == 1 ? weights[0] : Long.MAX_VALUE;
                        continue;
                    }

                    long res1 = mem[x - 1][y];
                    long res2 = mem[x - 1][y - 1];

                    if (res2 <= weights[x] * 6) {
                        res1 = Math.min(res1, res2 + weights[x]);
                    }

                    mem[x][y] = res1;
                }
            }

            int res = 1;
            for (int j = MAX_ANT; j >= 1; j--) {
                if (mem[n - 1][j] < Long.MAX_VALUE) {
                    res = j;
                    break;
                }
            }

            System.out.println("Case #" + i + ": " + res);
        }
    }
}