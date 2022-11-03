import java.util.function.*;

public class Interfaces {
    public static void main(String[] args) {
        System.out.println(predicateLambda("super long string"));
        primitivePredicate();
        consumer();
        function();
        System.out.println(supplier());
        bi();
        System.out.println(methodParams(x -> x + 5, 5));
    }   

    //***//Predicate//***//
    // a Predicate is a functional interface that can be used anywhere you need to evaluate a boolean condition
    public static boolean predicate() {
        Predicate<String> isALongWord = new Predicate<String>() {
            @Override
            public boolean test(String t) {
                return t.length() > 10;
            }
        };
        String s = "successfully";
        boolean result = isALongWord.test(s);
        return result;
    }

    //                                              predicate
    // List<String> filtered = l.stream().filter( s -> s.length() > 5 ).collect(Collectors.<String>toList());
    public static boolean predicateLambda(String word) {
        Predicate<String> isALongWord = t -> t.length() > 10;
        //new ArrayList<String>().stream().filter(isALongWord).collect(Collectors.<String>toList());
        return isALongWord.test(word);
    }

    public static void primitivePredicate() {
        IntPredicate greater = i -> i > 10;
        System.out.println(greater.test(12));
    }

    //***//Consumer//***//
    // represents an operation that accepts a single input argument and returns no result. The real outcome is the side-effects it produces
    public static class Product {
        private double price = 0.0;
      
        public void setPrice(double price) {
          this.price = price;
        }
      
        public void printPrice() {
          System.out.println(price);
        }
    }
      
    public static void consumer() {
        //IntConsumer
        Consumer<Product> updatePrice = p -> p.setPrice(5.9);
        Product p = new Product();
        updatePrice.accept(p); // performs this operation on the given argument
        p.printPrice();
        
        Consumer<Product> showPrice = s -> s.printPrice();
        Consumer<Product> updateAndShow = updatePrice.andThen(showPrice); // performs passed in consumer after original consumer
        updateAndShow.accept(p);
    }

    //***//Function//***//
    public static void function() {
        //IntToDoubleFunction
        Function<Integer, String> typeCast = val -> Integer.toString(val); // val -> val |TYPES| Integer -> String *NOTE does not automatically typecast
        System.out.println(typeCast.apply(5).getClass());
        
        Function<Integer, Integer> square = val -> val * val;
        System.out.println(square.apply(5));

        // f.andThen(Function) runs f first then param function
        // f.compose(Function) runs param function first then f
        // F.identity() returns T in apply(T)

        // When both generics of Function<> are the same type you can use UnaryOperator
        //IntUnaryOperator
        UnaryOperator<Double> increase = d -> d++;
        System.out.println(increase.apply(5.2));
    }
    
    //***//Supplier//***//
    // yep
    public static int supplier() {
        //IntSupplier
        Supplier<Integer> add = () -> 10;
        return add.get();
    }

    //***//Bi//***//
    public static void bi() {
        //ObjIntConsumer
        BiConsumer<Integer, Double> sum = (i, d) -> System.out.println(i + d);
        sum.accept(5, 2.3);

        //ToIntBiFunction
        BiFunction<Integer, Integer, Double> divide = (x1, x2) -> (double)x1/x2;
        System.out.println(divide.apply(5, 2));

        //IntBinaryOperator
        BinaryOperator<Integer> sub = (x1, x2) -> x1 - x2;
        System.out.println(sub.apply(5, 2)); // returns Integer

    }

    public static <T, R> R methodParams(Function<T, R> f, T num) {
        return f.apply(num);
    }
}
