package dev.omar.introduction;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeSort {
    public static List<Integer> mergeSort(List<Integer> arr) {
        if(arr.size() == 0) throw new Error("Faulty input");
        if(arr.size() == 1) return arr;

        int n = arr.size();
        int halfN = n/2;

        List<Integer> first = mergeSort(arr.subList(0, halfN));
        List<Integer> second = mergeSort(arr.subList(halfN, n ));
        List<Integer> complete = new ArrayList<>();

        int j = 0, l = 0;
        for (int i = 0; i < n; i++) {
            int a = j == first.size() ? Integer.MAX_VALUE : first.get(j);
            int b = l == second.size() ? Integer.MAX_VALUE : second.get(l);
            if(a < b) {
                complete.add(a);
                j++;
            } else {
                complete.add(b);
                l++;
            }
        }

        return complete;
    }

    public static void main(String[] args) {
        List<Integer> intList = new ArrayList<Integer>(Arrays.asList(3, 3, 3, 9, 3, 4, 10, 15));
        System.out.println("Original list: ");
        System.out.println(intList);
        List<Integer> sortedList = mergeSort(intList);
        System.out.println("Sorted list: ");
        System.out.println(sortedList);
    }
}
