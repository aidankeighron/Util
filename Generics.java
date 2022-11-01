import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Generics<A> {

    public static void main(String[] args) {
        // generic methods
        Generics<Integer> g = new Generics<Integer>();
        List<Integer> genericMethodInt = g.genericMethod(new Integer[]{0, 1, 2, 3, 4, 5});
        List<Double> genericMethodDouble = g.genericMethod(new Double[]{0.1, 1.5, 2.7, 3.2, 4.8, 5.6});

        System.out.println("Integer");
        for (Integer integer : genericMethodInt)
            System.out.print(integer + " ");
        System.out.println();
        System.out.println("Double");
        for (Double integer : genericMethodDouble)
            System.out.print(integer + " ");

        // array to list
        System.out.println();
        System.out.println("Sqrt");
        Integer[] array = {1, 4, 9, 16};
        Function<Integer, Double> sqrt = a -> Math.sqrt(a);
        List<Double> result = g.fromArrayToList(array, sqrt);
        result.forEach(e -> System.out.print(e + " "));

        //g.multipleBounds("Wrong Type"); // error
        g.multipleBounds(1); // number
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

    // public <T extends Number> List<T> fromArrayToList(T[] a) {

    // }

    //multiple bounds

    public <T extends Number & Comparable<T>> void multipleBounds(T boundedParam) {

    }

    // upper bound wildcards

    public void upperBoundWildcards(List<? extends String> buildings) {

    }

    // lower bound wildcard

    public void lowerBoundWildcard(List<? super A> exaple) {

    }
}
