# Viewing
Github pages site for easy viewing: [site](https://aidankeighron.github.io/Util/)

# Contributing
To contribute: make a pull request either adding concepts to an existing languages or adding a new language

## Adding a Language
- create a folder that is the same name as your language in the `docs/assets/` directory containing .md files with example scripts covering the aspects of your language

**EX .md file:**
~~~markdown
---
layout: script
language: Java
---

```java
public <T extends Number & Comparable<T>> void multipleBounds(T boundedParam) {

}
```
~~~
Make sure `layout` is `script` and `language` is the language the script belongs to. With the name of the file being the concept you are covering.
- add {your language}.md to docs/assets/languages 
```markdown
---
layout: language
---
```
Make sure `layout` is `language`. The name of the language should be the name of the file.
## Adding to a language
- add a .md with the name of the concept you would like to cover to the `docs/assets/{your language}` directory

**EX:**
~~~markdown
---
layout: script
language: Java
---

```java
public <T extends Number & Comparable<T>> void multipleBounds(T boundedParam) {

}
```
~~~
Make sure `layout` is `script` and `language` is the language the script belongs to. With the name of the file being the concept you are covering.
