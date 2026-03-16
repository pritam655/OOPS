'''Check if the string "Welcome to College" contains "College"'''
# public class ContainsExample1 {
#     public static void main(String[] args) {
#         String str = "Welcome to College";
#
#         if (str.contains("College")) {
#             System.out.println("The string contains 'College'");
#         } else {
#             System.out.println("The string does not contain 'College'");
#         }
#     }
# }

'''Check whether the string "Online Learning Platform" contains "Offline"'''
# public class ContainsExample2 {
#     public static void main(String[] args) {
#         String str = "Online Learning Platform";
#
#         if (str.contains("Offline")) {
#             System.out.println("The string contains 'Offline'");
#         } else {
#             System.out.println("The string does not contain 'Offline'");
#         }
#     }
# }

'''Find the index of character 'e' in the string "Welcome"'''
# public class IndexExample {
#     public static void main(String[] args) {
#         String str = "Welcome";
#
#         int index = str.indexOf('e');
#         System.out.println("Index of 'e' is: " + index);
#     }
# }

'''Print -1 if a substring is not found in the string'''
# public class SubstringCheck {
#     public static void main(String[] args) {
#         String str = "Java Programming";
#
#         int index = str.indexOf("Python");
#
#         System.out.println(index);   // prints -1 if not found
#     }
# }

'''Print the last position of 'e' in the string "Experience"'''
# public class LastIndexExample {
#     public static void main(String[] args) {
#         String str = "Experience";
#
#         int lastIndex = str.lastIndexOf('e');
#         System.out.println("Last index of 'e' is: " + lastIndex);
#     }
# }

'''Check whether the string "Information Technology" starts with "Tech"'''
# public class StartsWithExample {
#     public static void main(String[] args) {
#         String str = "Information Technology";
#
#         if (str.startsWith("Tech")) {
#             System.out.println("String starts with 'Tech'");
#         } else {
#             System.out.println("String does not start with 'Tech'");
#         }
#     }
# }

'''Check whether the string "Student Data File.txt" ends with ".txt"'''
# public class EndsWithExample {
#     public static void main(String[] args) {
#         String str = "Student Data File.txt";
#
#         if (str.endsWith(".txt")) {
#             System.out.println("File is a text file");
#         } else {
#             System.out.println("File is not a text file");
#         }
#     }
# }

'''Compare "Computer" and "computer" using equals() and equalsIgnoreCase()'''
# public class CompareStrings {
#     public static void main(String[] args) {
#         String str1 = "Computer";
#         String str2 = "computer";
#
#         System.out.println("Using equals(): " + str1.equals(str2));
#         System.out.println("Using equalsIgnoreCase(): " + str1.equalsIgnoreCase(str2));
#     }
# }

'''Take two strings from the user and check if they are equal ignoring case'''
# import java.util.Scanner;
# public class UserStringCompare {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
# 
#         System.out.print("Enter first string: ");
#         String str1 = sc.nextLine();
#
#         System.out.print("Enter second string: ");
#         String str2 = sc.nextLine();
#
#         if (str1.equalsIgnoreCase(str2)) {
#             System.out.println("Both strings are equal (ignoring case).");
#         } else {
#             System.out.println("Strings are not equal.");
#         }
#
#         sc.close();
#     }
# }