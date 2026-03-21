# Define a class employee with the following specification:
# ▪ Members are: empno of type integer, ename of type String, basic, hr and da are of type float, netpay of type float.
# ▪ Member functions:
# ▪ Calculate() : A function to find basix+hra+da with the float return type.
# ▪ havedata(): function to accept values for empno, ename, basic, hra, da and invoke calculate() to calculate netpay.
# ▪ dispdata(): function to display all the data members.


import java.util.Scanner;

class Employee {
    int empno;
    String ename;
    float basic, hra, da;
    float netpay;

    // Function to calculate net pay
    float calculate() {
        netpay = basic + hra + da;
        return netpay;
    }

    // Function to accept data
    void havedata() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Employee Number: ");
        empno = sc.nextInt();

        System.out.print("Enter Employee Name: ");
        ename = sc.next();

        System.out.print("Enter Basic Salary: ");
        basic = sc.nextFloat();

        System.out.print("Enter HRA: ");
        hra = sc.nextFloat();

        System.out.print("Enter DA: ");
        da = sc.nextFloat();

        calculate(); // calculate netpay
    }

    // Function to display data
    void dispdata() {
        System.out.println("\nEmployee Details:");
        System.out.println("Employee Number: " + empno);
        System.out.println("Employee Name: " + ename);
        System.out.println("Basic Salary: " + basic);
        System.out.println("HRA: " + hra);
        System.out.println("DA: " + da);
        System.out.println("Net Pay: " + netpay);
    }

    // Main method to test
    public static void main(String[] args) {
        Employee e = new Employee();
        e.havedata();
        e.dispdata();
    }
}