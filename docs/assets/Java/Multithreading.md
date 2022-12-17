---
layout: script
title: Multithreading
language: Java
---

```java
public class Multithreading {
    // THERE IS ALLOT MORE TO THREADS THAN THIS
    //https://www.geeksforgeeks.org/java-multithreading-tutorial/
    //https://www.netjstech.com/2015/05/java-advanced-topics.html
    public static void main(String[] args) {
        Extend object = new Extend();
        object.start();
        // object.yield();
        // object.interrupt();

        Thread thread = new Thread(new Implement());
        thread.start();
    }   

    /*
        Thread Class vs Runnable Interface 
        - If we extend the Thread class, our class cannot extend any other class because Java doesn’t support multiple inheritance. But, if we implement the Runnable interface, our class can still extend other base classes.
        - We can achieve basic functionality of a thread by extending Thread class because it provides some inbuilt methods like yield(), interrupt() etc. that are not available in Runnable interface.
        - Using runnable will give you an object that can be shared amongst multiple threads. 
     */
    
    public static class Extend extends Thread {
        public void run() {
            try {
                System.out.println("Thread "+Thread.currentThread().getId()+" is running");
            }
            catch (Exception e) {
                System.out.println("Exception is caught");
            }
        }
    }

    public static class Implement implements Runnable {

        @Override
        public void run() {
            try {
                System.out.println("Thread "+Thread.currentThread().getId()+" is running");
            }
            catch (Exception e) {
                System.out.println("Exception is caught");
            }
        }
    }
}
```