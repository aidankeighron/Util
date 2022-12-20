---
layout: script
language: Java
---

```java
//a simple program to demonstrate the use of stream in java
import java.util.*;
import java.util.stream.*;

public class Stream_ {

    public static void main(String[] args) {
        // create a list of integers
        List<Integer> number = Arrays.asList(2,3,4,5);
    
        // demonstration of map method
        List<Integer> square = number.stream().map(x -> x*x).
                            collect(Collectors.toList());
        System.out.println(square);
    
        // create a list of String
        List<String> names =
                    Arrays.asList("Reflection","Collection","Stream");
    
        // demonstration of filter method
        List<String> result = names.stream().filter(s->s.startsWith("S")).
                            collect(Collectors.toList());
        System.out.println(result);
    
        // demonstration of sorted method
        List<String> show =
                names.stream().sorted().collect(Collectors.toList());
        System.out.println(show);
    
        // create a list of integers
        List<Integer> numbers = Arrays.asList(2,3,4,5,2);
    
        // collect method returns a set
        Set<Integer> squareSet =
            numbers.stream().map(x->x*x).collect(Collectors.toSet());
        System.out.println(squareSet);
    
        // demonstration of forEach method
        number.stream().map(x->x*x).forEach(y->System.out.println(y));
    
        // demonstration of reduce method
        int even =
        number.stream().filter(x->x%2==0).reduce(0,(ans,i)-> ans+i); // Sum of even
        int evenbetter = number.stream().filter(x->x%2==0).reduce(0, Integer::sum);
    
        System.out.println(even);
        System.out.println(evenbetter);
    }

    public static void interfaces() {
        new ArrayList<>().stream().allMatch(null); // returns true if ALL elements match the predicate
        new ArrayList<>().stream().anyMatch(null); // return true if ANY elements match the predicate
        Stream.builder(); // This allows the creation of a Stream by generating elements individually and adding them to the Builder (without the copying overhead that comes from using an ArrayList as a temporary buffer.)
        new ArrayList<>().stream().collect(null); // performs mutable reduction using the collector
        new ArrayList<>().stream().collect(null, null, null); // preforms mutable reduction on the stream
        Stream.concat(null, null); // combine stream a and b (a is followed by b)
        new ArrayList<>().stream().count(); // number of elements in stream
        new ArrayList<>().stream().distinct(); // returns stream of unique elements
        Stream.empty(); // empty stream
        new ArrayList<>().stream().filter(null); // stream with elements that match the predicate
        new ArrayList<>().stream().findAny(); // random object of the first element of the stream
        new ArrayList<>().stream().findFirst(); // an object of the first element of the stream
        new ArrayList<>().stream().flatMap(null); // maps a stream using provided mapper /*Stream of every line in a file*/.flatMap(line -> Stream.of(line.split(" +")))
        new ArrayList<>().stream().flatMapToDouble(null); //ToInt | ToLong
        new ArrayList<>().stream().forEach(null); // performs and action on each element
        new ArrayList<>().stream().forEachOrdered(null); // performs action in the encounter order
        Stream.generate(null); // returns an infinite unordered stream using the supplier
        Stream.iterate(null, null); // returns an infinite ordered provided by f and the seed
        new ArrayList<>().stream().limit((Long) null); // return stream containing elements truncated to be no longer that max length
        new ArrayList<>().stream().map(null); // returns a stream with the results of applying the given function
        new ArrayList<>().stream().mapToDouble(null); // ToInt | ToLong
        new ArrayList<>().stream().max(null); // return the maximum element according to the comparator
        new ArrayList<>().stream().min(null); // return the minimum element according to the comparator
        new ArrayList<>().stream().noneMatch(null); // returns true if NO elements match the predicate
        Stream.of(1, 2); // returns a sequential ordered stream of provided elements
        Stream.of(1); // returns a sequential stream containing a single element
        new ArrayList<>().stream().peek(null);
        new ArrayList<>().stream().reduce(null);
        new ArrayList<>().stream().reduce(null, null); // accumulator.apply(identity, value) for each element
        new ArrayList<>().stream().skip((Long) null); // skips n elements of the stream
        new ArrayList<>().stream().sorted(); // sort stream in natural order
        new ArrayList<>().stream().sorted(null); // sort stream according to comparator
        new ArrayList<>().stream().toArray(); // returns a array of the stream elements
        new ArrayList<>().stream().toArray(null); // returns an array containing the elements using the generator as well as any additional arrays required for resizing
    }
}
```