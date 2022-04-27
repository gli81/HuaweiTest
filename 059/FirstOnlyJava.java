import java.util.*;

public class FirstOnlyJava{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        String line = "asdfasdfo";
        char[] l = new char[line.length()];
        HashMap<Character, Integer> m = new HashMap<Character, Integer>();

        char c;
        for (int i = 0; i < line.length(); i++) {
            c = line.charAt(i);
            l[i] = c;
            m.put(c, m.getOrDefault(c, 0) + 1);
        }
        Boolean flag = false;
        
        for (int i = 0; i < l.length; i++) {
            if (m.get(l[i]) == 1) {
                System.out.println(l[i]);
                flag = true;
                break;
            }
        }
        if (!flag) System.out.println("-1");
        sc.close();
    }
}