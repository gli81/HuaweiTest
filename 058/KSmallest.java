import java.util.Scanner;
import java.util.Arrays;

public class KSmallest {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int k, n;
        // n = scan.nextInt();
        // k = scan.nextInt();
        n = 5;
        k = 2;
        // int[] arr = new int[n];
        // for (int i = 0; i < n; i++) {
        //     arr[i] = scan.nextInt();
        // }
        int[] arr = new int[]{1, 3, 5, 7, 2};
        Arrays.sort(arr);
        for (int i = 0; i < k; i++) {
            System.out.print(arr[i]);
            if (i != k - 1) {
                System.out.print(" ");
            }
        }
        System.out.println();
        scan.close();
    }
}