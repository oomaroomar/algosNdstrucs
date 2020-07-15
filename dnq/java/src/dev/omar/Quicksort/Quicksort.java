package dev.omar.quicksort;

import java.io.File;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Quicksort {
   public static List<Integer> quickSort(List<Integer> arr) {

       return arr;
   }

   public static List<Integer> getList() {
      File file = new File("numbers.txt");
      Scanner sc = new Scanner(file);
      var numbers = new ArrayList<Integer>();

      while(sc.hasNextLine()) {
         numbers.add(sc.nextLine());
      }
   }

   public static void main(String[] args) {
      var numbers = getList();
      numbers = quickSort(numbers);
      Sys
   }
}
