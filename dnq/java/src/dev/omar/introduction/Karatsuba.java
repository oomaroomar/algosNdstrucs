package dev.omar.introduction;

import java.lang.Math;

public class Karatsuba {

    public static String add(String x, String y) {
        x = x.isEmpty() ? "0" : x;
        y = y.isEmpty() ? "0" : y;
        int xSize = x.length(), ySize = y.length();
        StringBuilder complete = new StringBuilder();
        int n = Math.max(xSize, ySize);
        int co = 0;

        for(int i = 1; i <= n; i++) {
            int xi = xSize - i, yi = ySize - i;
            int n1 = xi >= 0 ? Character.getNumericValue(x.charAt(xi)) : 0;
            int n2 = yi >= 0 ? Character.getNumericValue(y.charAt(yi)) : 0;
            int sum = n1 + n2 + co;
            int curD = sum % 10;
            co = (sum - curD)/10;
            complete.insert(0, curD);
        }
        if (co > 0) complete.insert(0, co);

        return complete.toString();
    }

    public static String subtract(String x, String y) {
        x = x.isEmpty() ? "0" : x;
        y = y.isEmpty() ? "0" : y;
        int xSize = x.length(), ySize = y.length();
        int n = Math.max(xSize, ySize);
        // 0 = unset, 1 = first input, 2 = second input
        int larger =
            xSize > ySize ? 1
            : ySize > xSize
            ? 2 : 0;

        if (larger == 0) {
            for (int i = 0; i < n; i++) {
                int n1 = i > xSize-1 ? 0 : Character.getNumericValue(x.charAt(i));
                int n2 = i > ySize-1 ? 0 : Character.getNumericValue(y.charAt(i));
                if (n1 > n2) {
                    larger = 1;
                    break;
                }
                if (n2 > n1) {
                    larger = 2;
                    break;
                }
            }
        }
        if (larger == 0) return "0";
        return larger == 1 ? countSubtraction(x, y, n) : '-' + countSubtraction(y, x, n);
    }

    public static String countSubtraction(String larger, String smaller, int n) {
        StringBuilder complete = new StringBuilder();
        int sSize = smaller.length();
        int co = 0;
        for(int i = 0; i < n; i++) {
            int n1 = Character.getNumericValue(larger.charAt(n-1-i));
            int n2 = i > sSize-1 ? 0 : Character.getNumericValue(smaller.charAt(sSize-1-i));
            int sum = n1 - n2 - co;
            if(sum < 0) {
                co = 1;
                sum += 10;
            } else {
                co = 0;
            }
            complete.insert(0, sum);
        }
        while(complete.charAt(0) == '0') {
            complete.deleteCharAt(0);
        }
       return complete.toString();
    }

    public static String multiply(String x, String y) {
        int xSize = x.length();
        int ySize = y.length();
        int n = Math.max(xSize, ySize);

        if (n <= 3){
            int itnX = x.isEmpty() ? 0 : Integer.parseInt(x);
            int intY = y.isEmpty() ? 0 : Integer.parseInt(y);
            return Integer.toString(itnX * intY);
        }

        int halfN = (n/2) + (n%2);
        int halfX = (xSize/2) + (xSize%2);
        int halfY = (ySize/2) + (ySize%2);

        String a = x.substring(0, halfX);
        String b = x.substring(halfX, xSize);
        String c = y.substring(0, halfY);
        String d = y.substring(halfY, ySize);

        String ac = multiply(a, c);
        String bd = multiply(b, d);

        String aPb = add(a, b);
        String cPd = add(c, d);
        String aPbMcPd = multiply(aPb, cPd);
        String tto = subtract(subtract(aPbMcPd , ac), bd);

        String first = addZeroes(ac, 2*halfN);
        String scnd = addZeroes(tto, halfN);
        String wave1 = add(first, bd);
        String wave2 = add(wave1, scnd);
        return wave2;
    }

    public static String addZeroes(String s, int n) {
        StringBuilder builder = new StringBuilder(s);
        for(int i = 0; i < n; i++) {
            builder.append('0');
        }
        return builder.toString();
    }

    public static void main(String[] args) {
//        String n1 = "3141592653589793238462643383279502884197169399375105820974944592";
//        String n2 = "2718281828459045235360287471352662497757247093699959574966967627";
        String n1 = "213546111";
        String n2 = "124365111";
        String product = multiply(n1, n2);
        System.out.println("\nProduct : "+ product);
    }
}
