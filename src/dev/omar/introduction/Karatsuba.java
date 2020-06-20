package dev.omar.introduction;

import java.lang.Math;

public class Karatsuba {

    public static String add(String x, String y) {
        int xSize = x.length(), ySize = y.length();
        StringBuilder complete = new StringBuilder();
        int n = Math.max(xSize, ySize);
        int co = 0;

        for(int i = 1; i <= n; i++) {
            int xi = xSize - i, yi = ySize - i;
            int n1 = xi >= 0 ? Character.getNumericValue(x.charAt(xi)) : 0;
            int n2 = xi >= 0 ? Character.getNumericValue(y.charAt(yi)) : 0;
            int sum = n1 + n2 + co;
            int curD = sum % 10;
            co = sum - curD;
            complete.insert(0, curD);
        }
        if (co > 0) complete.insert(0, co);

        return complete.toString();
    }
    public static String addZeroes(int i, int j, String s) {
        StringBuilder builder = new StringBuilder(s);
        while (i < j) {
            builder.insert(0, '0');
            i++;
        }
        return builder.toString();
    }

    public static String subtract(String x, String y) {
        int xSize = x.length(), ySize = y.length();
        int n = Math.max(xSize, ySize);
        // 0 = unset, 1 = first input, 2 = second input
        int larger = 0;
        if (xSize > ySize) {
            larger = 1;
            y = addZeroes(ySize, xSize, y);
        }
        if (ySize > xSize) {
            larger = 2;
            x = addZeroes(xSize, ySize, x);
        }
        if (larger == 0) {
            for (int i = 0; i < n; i++) {
                int n1 = Character.getNumericValue(x.charAt(i));
                int n2 = Character.getNumericValue(y.charAt(i));
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
        String complete;

        if (larger == 1) {
            complete = countSubtraction(x, y, n);
        } else {
            complete = countSubtraction(y, x, n);
            complete = '-' + complete;
        }
        return complete;
    }

    public static String countSubtraction(String larger, String smaller, int n) {
        StringBuilder complete = new StringBuilder();
        int co = 0;

        for(int i = n-1; i >= 0; i--) {
            int n1 = Character.getNumericValue(larger.charAt(i));
            int n2 = Character.getNumericValue(smaller.charAt(i));
            int sum = n1 - n2 - co;
            if(sum < 0) {
                co = 1;
                sum += 10;
            } else {
                co = 0;
            }
            complete.insert(0, sum);
        }
        return complete.toString();
    }

    public static String multiply(String x, String y) {
        int xSize = x.length();
        int ySize = y.length();
        int n = Math.max(xSize, ySize);

        if (n == 3){
            int num = Integer.parseInt(x) * Integer.parseInt(y);
            return Integer.toString(num);
        }
        x = xSize == n ? x : addZeroes(xSize, n, x);
        y = ySize == n ? y : addZeroes(ySize, n, y);

        int halfN = (n/2) + (n%2);
        long m = (long) Math.pow(10, halfN);

        String a = x.substring(0, halfN);
        String b = addZeroes(xSize/2, halfN, x.substring(halfN, n));
        String c = y.substring(0, halfN);
        String d = addZeroes(ySize/2, halfN, y.substring(halfN, n));

        String ac = multiply(a, c);
        String bd = multiply(b, d);
        String aPbMcPd = multiply(add(a , b), add(c , d));
        String tto = subtract(subtract(aPbMcPd , ac), bd);

        // Putting all this shit inline was probably a mistake
        return add(add(multiply(ac, String.valueOf((long)Math.pow(10, 2*halfN))), bd), multiply(tto, String.valueOf(m)));
//        return ac * (Math.pow(10, 2*halfN)) + bd + tto * m;
    }

    public static int getSize(long num) {
       int size = 0;
       do {
            num /= 10;
            size++;
       } while (num >= 1);

       return size;
    }

    public static void main(String[] args) {
        //String n1 = "3141592653589793238462643383279502884197169399375105820974944592";
        //String n2 = "2718281828459045235360287471352662497757247093699959574966967627";
        String n1 = "311";
        String n2 = "3111";
        String product = multiply(n1, n2);
        System.out.println("\nProduct : "+ product);
    }
}
