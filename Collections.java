import java.util.*;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentSkipListSet;
import java.util.concurrent.CopyOnWriteArraySet;

public class Collections {
    //https://www.geeksforgeeks.org/collections-in-java-2/?ref=lbp
    //https://javarevisited.blogspot.com/2020/04/how-to-choose-right-type-of-collection.html
    //http://www.javapractices.com/topic/TopicAction.do?Id=65
    //https://docs.oracle.com/javase/8/docs/technotes/guides/collections/index.html
    //https://docs.oracle.com/javase/tutorial/collections/interfaces/index.html
    //http://www.javapractices.com/home/HomeAction.do

    //use List if you need an array-like data structure and you need to iterate over the elements
    //use Map if you need something like a dictionary
    //use a Set if you only need to decide if something belongs to the set or not.

    // List
    ArrayList arrayList;
    LinkedList linkedList;

    // Set
    HashSet hashSet;
    LinkedHashSet linkedHashSet;
    TreeSet treeSet;
    EnumSet enumSet;
    CopyOnWriteArraySet copyOnWriteArraySet;
    ConcurrentSkipListSet concurrentSkipListSet;

    // Map
    HashMap hashMap;
    LinkedHashMap linkedHashMap;
    TreeMap treeMap;
    Hashtable hashTable;

    // Queue
    PriorityQueue priorityQueue;
    BlockingQueue blockingQueue;
}
