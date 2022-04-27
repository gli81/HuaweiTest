import java.util.Scanner;
import java.lang.Math;
import java.lang.StringBuilder;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str1 = "623192091";
        String str2 = "14426202982932";

        // different length
        int diff = Math.abs(str1.length() - str2.length());
        if (str1.length() > str2.length()) {
            for (int i = 0; i < diff; i++) {
                str2 = "0" + str2;
            }
        } else {
            for (int i = 0; i < diff; i++) {
                str1 = "0" + str1;
            }
        }

        char[] chrs1 = str1.toCharArray();
        int l = chrs1.length;
        char[] chrs2 = str2.toCharArray();
        int[] ansArray = new int[l + 1];
        for (int i = 0; i < l; i++) {
            ansArray[i + 1] = Integer.parseInt(String.valueOf(chrs1[i])) + Integer.parseInt(String.valueOf(chrs2[i]));
        }
        for (int i = 0; i < ansArray.length; i++) {
            if (ansArray[ansArray.length - i - 1] >= 10) {
                ansArray[ansArray.length - i - 2]++;
                ansArray[ansArray.length - i - 1] -= 10;
            }
        }
        char[] charArray = new char[l + 1];
        for (int i = 0; i < ansArray.length; i++) {
            charArray[i] = (char)(ansArray[i] + 48);
        }
        StringBuilder ans = new StringBuilder(new String(charArray));
        if (ans.charAt(0) == '0') ans.deleteCharAt(0);
        System.out.println(ans);
        scan.close();
    }
}