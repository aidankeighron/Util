---
layout: script
title: Annotations
language: Java
---

```json
Annotations applied to Java code:

  /**
  * Change the contents of a text file in its entirety, overwriting any
  * existing text.
  *
  * @param file is an existing file (not a directory) which can be written.
  * @param contents is the text to be placed into aFile.
  *
  * @exception FileNotFoundException if file does not exist.
  * @exception IOException if stream to file cannot be written to or closed.
  *
  * @exception IllegalArgumentException if file is a directory.
  * @exception IllegalArgumentException if file cannot be written.
  * @exception SecurityException if a SecurityManager exists and
  * disallows read or write access to aFile.
  */

@Override - Checks that the method is an override. Causes a compilation error if the method is not found in one of the parent classes or implemented interfaces.
@Deprecated - Marks the method as obsolete. Causes a compile warning if the method is used.
@SuppressWarnings - Instructs the compiler to suppress the compile time warnings specified in the annotation parameters.
Annotations applied to other annotations (also known as "Meta Annotations"):

@Retention - Specifies how the marked annotation is stored, whether in code only, compiled into the class, or available at runtime through reflection.
@Documented - Marks another annotation for inclusion in the documentation.
@Target - Marks another annotation to restrict what kind of Java elements the annotation may be applied to.
@Inherited - Marks another annotation to be inherited to subclasses of annotated class (by default annotations are not inherited by subclasses).
Since Java 7, three additional annotations have been added to the language.

@SafeVarargs - Suppress warnings for all callers of a method or constructor with a generics varargs parameter, since Java 7.
@FunctionalInterface - Specifies that the type declaration is intended to be a functional interface, since Java 8.
@Repeatable - Specifies that the annotation can be applied more than once to the same declaration, since Java 8.
```