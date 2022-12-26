import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Generics<A> {

    public static void main(String[] args) {
        // generic methods
        Generics<Integer> g = new Generics<Integer>();
        List<Integer> genericMethodInt = g.genericMethod(new Integer[]{0, 1, 2, 3, 4, 5});
        List<Double> genericMethodDouble = g.genericMethod(new Double[]{0.1, 1.5, 2.7, 3.2, 4.8, 5.6});

        System.out.print("Integer: ");
        for (Integer integer : genericMethodInt) // 0 1 2 3 4 5
            System.out.print(integer + " ");
        System.out.println();
        System.out.print("Double: ");
        for (Double integer : genericMethodDouble) // 0.1 1.5 2.7 3.2 4.8 5.6
        System.out.print(integer + " ");
        System.out.println();

        // array to list
        System.out.print("Sqrt: ");
        Integer[] array = {1, 4, 9, 16};
        Function<Integer, Double> sqrt = a -> Math.sqrt(a);
        List<Double> result = g.fromArrayToList(array, sqrt);
        result.forEach(e -> System.out.print(e + " ")); // 1.0 2.0 3.0 4.0

        g.fromArrayToList(new Integer[]{1, 2, 3, 4, 5}); // parameter extends Number

        //g.multipleBounds("Wrong Type"); // error // parameter does not extend bounds
        g.multipleBounds(1); // parameter extends Number


        g.upperBoundWildcards(new ArrayList<String>()); // String is hight than Object

        g.lowerBoundWildcard(new ArrayList<Object>()); // Object is lover than Integer
    }

    // generic methods
    public <T> List<T> genericMethod(T[] a) {   
        return Arrays.stream(a).collect(Collectors.toList());
    }

    // array to list
    public /*Don't need A here*/<G> List<G> fromArrayToList(A[] a, Function<A, G> mapperFunction) {
        return Arrays.stream(a)
        .map(mapperFunction)
        .collect(Collectors.toList());
    }

    // bounded generics

    public <T extends Number> List<T> fromArrayToList(T[] a) {
        return Arrays.stream(a).collect(Collectors.toList());
    }

    //multiple bounds

    public <T extends Number & Comparable<T>> void multipleBounds(T boundedParam) {

    }

    // upper bound wildcards

    public void upperBoundWildcards(List<? extends Object> buildings) {

    }

    // lower bound wildcard

    public void lowerBoundWildcard(List<? super A> exaple) {

    }

    //***//Wildcards//***//
    // if you want to be able to pass in List<Integer>, List<Double>, and List<Long>
    // if you try to pass in List<Boolean> you will get an error
    public void upper(List<? extends Number> list) {

    }

    // if you want to be able to pass in List<Integer>, List<Object>, and List<Number>
    // if you try to pass in List<Double> you will get an error
    public void lower(List<? super Integer> list) {

    }

    // can only use methods from the Object class
    public void none(List<?> list) {
        
    }
}
