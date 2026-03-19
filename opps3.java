// Define a class CARRENTAL with the following details:
// Class Members are: CarId of int type, CarType of string type and Rent of float type.
//  Define GetCar() method which accepts CarId and CarType.
//  GetRent() method which return rent of the car on the basis of car type, i.e. Small Car = 1000, Van = 800, SUV = 2500
//  ShowCar() method which allow user to view the contents of cars i.e. id, type and rent.

#include <iostream>
#include <string>
using namespace std;

class CARRENTAL
{
private:
    int CarId;
    string CarType;
    float Rent;

public:
    // Method to accept CarId and CarType
    void GetCar(int id, string type)
    {
        CarId = id;
        CarType = type;
    }

    // Method to calculate and return rent based on CarType
    float GetRent()
    {
        if (CarType == "Small Car")
            Rent = 1000;
        else if (CarType == "Van")
            Rent = 800;
        else if (CarType == "SUV")
            Rent = 2500;
        else
            Rent = 0; // default if type not matched

        return Rent;
    }

    // Method to display car details
    void ShowCar()
    {
        cout << "Car ID: " << CarId << endl;
        cout << "Car Type: " << CarType << endl;
        cout << "Rent: " << Rent << endl;
    }
};

// Example usage
int main()
{
    CARRENTAL c;
    c.GetCar(101, "SUV");
    c.GetRent();
    c.ShowCar();
    return 0;
}

// Define a class Resort with the following description:
// ▪ Members are: RNo to store Room Number, Name store customer name, Charges to store per day charges, Days to store number of days of stay.
// ▪ Member functions:
// ▪ Compute() to calculate and return Amount as Days * Charges and if the values of Days*Charges is more than 11000 then as 1.02*Days*Charges
// ▪ Getinfo() A function to enter the content Rno, Name, Charges and Days.
// ▪ DispInfo() A function to enter the content Rno, Name, Charges, Days and Amount by calling function Compute().

class Resort:
    def __init__(self):
        self.RNo = 0
        self.Name = ""
        self.Charges = 0
        self.Days = 0

    # Function to calculate amount
    def Compute(self):
        amount = self.Days * self.Charges
        if amount > 11000:
            amount = 1.02 * amount
        return amount

    # Function to get input
    def Getinfo(self):
        self.RNo = int(input("Enter Room Number: "))
        self.Name = input("Enter Customer Name: ")
        self.Charges = float(input("Enter Charges per day: "))
        self.Days = int(input("Enter Number of days: "))

    # Function to display details
    def DispInfo(self):
        amount = self.Compute()
        print("\n--- Resort Details ---")
        print("Room Number:", self.RNo)
        print("Customer Name:", self.Name)
        print("Charges per day:", self.Charges)
        print("Days Stayed:", self.Days)
        print("Total Amount:", amount)


# Create object and call functions
r = Resort()
r.Getinfo()
r.DispInfo()