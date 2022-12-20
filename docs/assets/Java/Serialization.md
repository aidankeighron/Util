---
layout: script
language: Java
---

```java
// Java code for serialization and deserialization 
// of a Java object
import java.io.*;
  

/*
 * Description for Output:
You have seen while deserializing the object the values of a and b has changed. The reason being a was marked as transient and b was static.
In case of transient variables:- A variable defined with transient keyword is not serialized during serialization process.This variable will 
be initialized with default value during deserialization. (e.g: for objects it is null, for int it is 0).
In case of static Variables:- A variable defined with static keyword is not serialized during serialization process.
This variable will be loaded with current value defined in the class during deserialization.

Points to remember
1. If a parent class has implemented Serializable interface then child class doesn’t need to implement it but vice-versa is not true.
2. Only non-static data members are saved via Serialization process.
3. Static data members and transient data members are not saved via Serialization process.So, if you don’t want to save value of a non-static data member then make it transient.
4. Constructor of object is never called when an object is deserialized.
5. Associated objects must be implementing Serializable interface.
Example :
 */
class Emp implements Serializable {
private static final long serialversionUID =
                                 129348938L;
    transient int a;
    static int b;
    String name;
    int age;
  
    // Default constructor
public Emp(String name, int age, int a, int b)
    {
        this.name = name;
        this.age = age;
        this.a = a;
        this.b = b;
    }
}
  
public class Serialization {
public static void printData(Emp object1)
    {
  
        System.out.println("name = " + object1.name);
        System.out.println("age = " + object1.age);
        System.out.println("a = " + object1.a);
        System.out.println("b = " + object1.b);
    }
  
public static void main(String[] args)
    {
        Emp object = new Emp("ab", 20, 2, 1000);
        String filename = "serialization.txt";
  
        // Serialization
        try {
  
            // Saving of object in a file
            FileOutputStream file = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(file);
  
            // Method for serialization of object
            out.writeObject(object);
  
            out.close();
            file.close();
  
            System.out.println("Data before Deserialization.");
            printData(object);
  
            // value of static variable changed
            object.b = 2000;
        }
  
        catch (Exception e) {
            e.printStackTrace();
        }
  
        object = null;
  
        // Deserialization
        try {
            // Reading the object from a file
            FileInputStream file = new FileInputStream(filename);
            ObjectInputStream in = new ObjectInputStream(file);
  
            // Method for deserialization of object
            object = (Emp)in.readObject();
  
            in.close();
            file.close();
            System.out.println("Data after Deserialization.");
            printData(object); 
        }
  
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```