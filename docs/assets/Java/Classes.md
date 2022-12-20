---
layout: script
language: Java
---

```java
public class Classes extends Object {

    private int var1;
    private String var2;

    public Classes(int var1, String var2) {
        this.var1 = var1;
        this.var2 = var2;
    }

    @Override
    public boolean equals(Object obj) {
    if (this == obj)
        return true;
      if (obj == null)
        return false;
      if (getClass() != obj.getClass())
          return false;
      Classes other = (Classes) obj;
      if (var1 != other.var1)
        return false;
      if (var2 == null) {
        if (other.var2 != null)
          return false;
      } else if (!var2.equals(other.var2))
          return false;
      return true;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + var1;
        result = prime * result
                + ((var2 == null) ? 0 :   var2.hashCode());
        return result;
    }
}
```