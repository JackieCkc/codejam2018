import java.util.*;
import java.io.*;

public class AntStackSmall {
    public static int dp(int[] weights, int totalWeight, int x, int y, int[][] mem) {
        y = Math.min(totalWeight, y);

        if (x == 0) {
            return weights[0] <= y ? 1 : 0;
        }

        if (mem[x][y] != -1) {
            return mem[x][y];
        }

        int max1 = -1;
        if (y >= weights[x]) {
            max1 = 1 + dp(weights, totalWeight, x - 1, Math.min(y - weights[x], 6 * weights[x]), mem);
        }

        int res = Math.max(max1, dp(weights, totalWeight, x - 1, y, mem));

        mem[x][y] = res;
        return res;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();

        for (int i = 1; i <= t; i++) {
            int n = in.nextInt();

            int[] weights = new int[n];
            int totalWeight = 0;
            for (int j = 0; j < n; j++) {
                int w = in.nextInt();
                weights[j] = w;
                totalWeight += w;
            }

            int[][] mem = new int[weights.length][totalWeight + 1];

            for (int j = 0; j < weights.length; j++) {
                for (int k = 0; k < totalWeight + 1; k++) {
                    mem[j][k] = -1;
                }
            }

            System.out.println("Case #" + i + ": " + dp(weights, totalWeight, weights.length - 1, totalWeight, mem));
        }
    }
}