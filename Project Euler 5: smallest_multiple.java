import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = Integer.parseInt(scanner.nextLine());
        for (int a0 = 0; a0 < t; a0++) {
            int n = Integer.parseInt(scanner.nextLine());
            System.out.println(lcmOfRange(n));
        }
        scanner.close();
    }

    private static long lcmOfRange(int n) {
        long lcm = 1;
        for (int i = 2; i <= n; i++) {
            lcm = lcm(lcm, i);
        }
        return lcm;
    }

    private static long gcd(long a, long b) {
        while (b > 0) {
            long temp = b;
            b = a % b; // % is remainder
            a = temp;
        }
        return a;
    }

    private static long lcm(long a, long b) {
        return a * (b / gcd(a, b));
    }
}
