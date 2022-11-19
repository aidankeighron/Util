import java.util.*;
import java.util.concurrent.*;

public class Collections {
    //https://www.geeksforgeeks.org/collections-in-java-2/?ref=lbp
    //https://javarevisited.blogspot.com/2020/04/how-to-choose-right-type-of-collection.html
    //http://www.javapractices.com/topic/TopicAction.do?Id=65

    //use List if you need an array-like data structure and you need to iterate over the elements
    //use Map if you need something like a dictionary
    //use a Set if you only need to decide if something belongs to the set or not. 

    // List //
    static ArrayList arrayList; // Dynamic Array | Fast for accessing specific element | Slow to add and remove element
    static LinkedList linkedList; // Dynamic Array | Fast for adding and deleting element | Slow to access specific element
    static Vector vector; // Dynamic Array | Identical to ArrayList but is synchronized | Rare to use in a non-thread environment
    static Stack stack; // Last in first out | Subclass of Vector | thread-safe but legacy class if thread safety is not needed use ArrayDeque
    
    // Queue
    // Deque // Double ended queue | and/remove elements from both ends of array
    static ArrayDeque arrayDeque; // Last in first out or First in first out | Subclass of vector
    static PriorityQueue priorityQueue; // First in first out | Custom sorting
    static BlockingDeque blockingDeque; // Deque but it does not allow illegal operations like deleting from an empty queue
    static PriorityBlockingQueue priorityBlockingQueue; // PriorityQueue but its blocking
    static ArrayBlockingQueue arrayBlockingQueue; // Size of queue is static | First in first out | blocking
    static DelayQueue delayQueue; // First in first out | delay on indexes
    static LinkedBlockingQueue linkedBlockingQueue; // First in first out | Can have a static length | blocking
    static LinkedBlockingDeque linkedBlockingDeque; // Deque but blocking

    // Set // No duplicates
    static ConcurrentHashMap concurrentHashMap;
    static HashSet hashSet; // Objects inserted do not guarantee to be returned in the same order | Inserted based on hashcode | allows null elements
    static LinkedHashSet linkedHashSet; // Doubly linked HashSet | Inserted based on order
    static TreeSet treeSet; // Tree storage | Ordering of elements is maintained using a set or provided comparator
    static EnumSet enumSet; // Static class for use with arrays of enums
    
    // Map // No duplicates
    static HashMap hashMap; // (Key, Value) pair
    static LinkedHashMap linkedHashMap;// Keeps track of the order elements were added in
    static TreeMap treeMap;// TreeSet but map | Duplicated allowed
    static Hashtable hashTable; // HashMap but you can specify number of elements and fillRatio
    static EnumMap enumMap; // Enum set but map
    static Properties properties; // System/Custom properties | File with string = string
    
    // Iterator
    // Fail-Fast // throws ConcurrentModificationException if the collection is modified while iterating\
    // Weakly consistent // Will not throw C... | Guaranteed to traverse elements as they existed but may or may not reflect modifications
    // Snapshot/Fail-Safe // Will not throw C... | Iterates over the original array only

    // ArrayList //
    public static void arrayList() {
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        arrayList.add(13);
        arrayList.add(7);
        arrayList.add(4);
        arrayList.add(1);
        arrayList.remove(2);
        System.out.println(arrayList);
    }

    // Linked List //
    public static void linkedList() {
        LinkedList<String> linkedList = new LinkedList<String>();
        linkedList.add("Linked");
        linkedList.add("lists");
        linkedList.add("are fast");
        linkedList.add("for adding");
        linkedList.removeFirst();
        System.out.println(linkedList);
    }

    // Vector //
    public static void vector() {
        Vector<Double> vector = new Vector<Double>();
        vector.add(0.5);
        vector.add(2.7);
        vector.add(4.1);
        vector.add(6.2);
        vector.remove(2);
        System.out.println(vector);
    }

    // Stack //
    public static void stack() {
        Stack<String> stack = new Stack<String>();
        stack.push("Java");
        stack.push("is");
        stack.push("really");
        stack.push("cool");
        Iterator<String> itr = stack.iterator(); // Fail-fast
        while(itr.hasNext()) {
            System.out.print(itr.next()+" ");
        }
        System.out.println();
        stack.pop();
        itr = stack.iterator();
        while (itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
        System.out.println();
    }

    // Array Deque //
    public static void arrayDeque() {
        ArrayDeque<String> arrayDeque = new ArrayDeque<String>();
        arrayDeque.push("Java");
        arrayDeque.push("is");
        arrayDeque.push("really");
        arrayDeque.push("cool");
        // Stack .getFirst() .pop()
        Iterator<String> itr = arrayDeque.descendingIterator(); // Fail-fast
        while(itr.hasNext()) {
            System.out.print(itr.next()+" ");
        }
        System.out.println();
        // Queue .getLast() .poll()
        itr = arrayDeque.iterator();
        while (itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
        System.out.println();
    }

    // Priority Queue //
    public static void priorityQueue() {
        Comparator<Double> comparator = (x, y) -> {
            if (x > y) {
                return 1;
            }
            else if (x < y) {
                return -1;
            }
            else {
                return 0;
            }
        };
        PriorityQueue<Double> priorityQueue = new PriorityQueue<Double>(comparator);
        priorityQueue.add(0.7);
        priorityQueue.add(1.2);
        priorityQueue.add(5.6);
        priorityQueue.add(4.3);
        System.out.println(priorityQueue.peek());
    }

    // Hash Set //
    public static void hashSet() {
        HashSet<String> hashSet = new HashSet<String>();
        hashSet.add("Programming");
        hashSet.add("is");
        hashSet.add("very");
        hashSet.add("very");
        hashSet.add("fun");

        Iterator<String> itr = hashSet.iterator(); // Fail-fast
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
    }

    // Tree Set //
    public static void treeSet() {
        TreeSet<Integer> treeSet = new TreeSet<Integer>();
        treeSet.add(5);
        treeSet.add(1);
        treeSet.add(3);
        treeSet.add(7);
        treeSet.add(2);
        treeSet.add(2);
        Iterator<Integer> itr = treeSet.iterator();
        while ( itr.hasNext()) {
            System.out.println(itr.next());
        }
        System.out.println(treeSet.ceiling(4));
        System.out.println(treeSet.headSet(5));
    }

    // Hash Map //
    public static void hashMap() {
        HashMap<Integer, String> hashMap = new HashMap<Integer, String>();
        hashMap.put(1, "Java");
        hashMap.put(5, "is");
        hashMap.put(7, "programming");

        System.out.println(hashMap.get(1));

        for (Map.Entry<Integer, String> e : hashMap.entrySet())
            System.out.println(e.getKey() + " " + e.getValue());
    }

    // Enum Set //
    enum Code { CODE, LEARN, CONTRIBUTE, QUIZ, MCQ };
    public static void enumSet() {
        EnumSet<Code> set1, set2, set3, set4;
 
        // Adding elements
        set1 = EnumSet.of(Code.QUIZ, Code.CONTRIBUTE, Code.LEARN, Code.CODE);
        set2 = EnumSet.complementOf(set1);
        set3 = EnumSet.allOf(Code.class);
        set4 = EnumSet.range(Code.CODE, Code.CONTRIBUTE);
 
        System.out.println("Set 1: " + set1);
        System.out.println("Set 2: " + set2);
        System.out.println("Set 3: " + set3);
        System.out.println("Set 4: " + set4);
    }

    // Delay Queue //
    static class DelayObject implements Delayed {
        private String name;
        private long time;
     
        public DelayObject(String name, long delayTime)
        {
            this.name = name;
            this.time = System.currentTimeMillis()
                        + delayTime;
        }
     
        @Override
        public long getDelay(TimeUnit unit)
        {
            long diff = time - System.currentTimeMillis();
            return unit.convert(diff, TimeUnit.MILLISECONDS);
        }
     
        @Override
        public int compareTo(Delayed obj)
        {
            if (this.time < ((DelayObject)obj).time) {
                return -1;
            }
            if (this.time > ((DelayObject)obj).time) {
                return 1;
            }
            return 0;
        }
     
        @Override
        public String toString()
        {
            return "\n{"+"name="+name+", time="+time+"}";
        }
    }
    public static void delayQueue() {
        BlockingQueue<DelayObject> delayQueue = new DelayQueue<DelayObject>();
        delayQueue.add(new DelayObject("A", 1));
        delayQueue.add(new DelayObject("B", 2));
        delayQueue.add(new DelayObject("C", 3));
        delayQueue.add(new DelayObject("D", 4));

        System.out.println("DelayQueue: "+delayQueue);
        BlockingQueue<DelayObject> DQ2 = new DelayQueue<DelayObject>(delayQueue);
        System.out.println("DelayQueue: "+DQ2);
    }

    public static void collections() {
        java.util.Collections.addAll(null); // Insert the specified collection elements into the specified collection
        java.util.Collections.asLifoQueue(null); // returns a view of a deque as a Lifo queue (Last in First out)
        java.util.Collections.binarySearch(null, null); // searches the key using binary search in list
        java.util.Collections.checkedCollection(null, null); // this method returns a dynamically type-safe view of the specified collection   
        java.util.Collections.copy(null, null); // copies all of the elements from one list to another
        java.util.Collections.disjoint(null, null); // this method returns true if the elements have no elements in common
        java.util.Collections.emptyList(); // empty list
        java.util.Collections.enumeration(null); // an enumeration over the collection
        java.util.Collections.fill(null, null); // replaces all of the elements of the specified list with the specified element
        java.util.Collections.frequency(null, null); // returns the number of elements in the specified collection equal to the specified object 
        java.util.Collections.indexOfSubList(null, null); // returns starting position of the first occurrence of the specified target list within the list or -1 if it does not exist
        java.util.Collections.list(null); // returns a list containing the elements returned by the specified enumeration in the order they are returned by the enumeration
        java.util.Collections.max(null, null); // returns the max elements according to the comparator
        java.util.Collections.nCopies(0, null); // returns an immutable list of copies of the object
        java.util.Collections.newSetFromMap(null); // returns set backed by the specified map
        java.util.Collections.replaceAll(null, null, null); // replaces all occurrences of one value with another
        java.util.Collections.reverse(null); // reverses the list
        java.util.Collections.reverseOrder(); // returns a comparator that imposes the revers of the natural ordering
        java.util.Collections.rotate(null, 0); // rotates the elements a specified distance
        java.util.Collections.shuffle(null); // randomizes the elements
        java.util.Collections.singleton(null); // returns an immutable map, mapping only the specified key to the specified value
        java.util.Collections.sort(null); // sorts the list according to the comparator
        java.util.Collections.swap(null, 0, 0); // swaps the elements at the specified positions
        java.util.Collections.synchronizedCollection(null); // returns a synchronized collection backed by the specified collection
        java.util.Collections.unmodifiableCollection(null); // returns an unmodifiable view of the specified collection
    }

    public static void main(String[] args) {
        arrayList();
        linkedList();
        vector();
        stack();
        arrayDeque();
        priorityQueue();
        hashSet();
        treeSet();
        hashMap();
        enumSet();
        delayQueue();
    }
}
