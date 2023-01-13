1 a) Variables of equal value of str and int objects have the same id
  ```python
  >>> python s1 = "Best School"
  >>> s2 = "Best School"
  >>> print(s1 is s2)
  True
  ```
  
  b) Variables of equal value of list objects do not have the same id
  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = [1, 2, 3]
  >>> print(l1 is l2)
  False
  ```

2 a) Adding to a list with append() or += does not change its id
  ```python
  >>> l1 = [1, 2, 3]
  >>> id(l1)
  0x001
  >>> l1.append(4)
  >>> id(l1)
  0x002
  ```
  
  b) Adding to a list with = changes its id
  ```python
  >>> l1 = [1, 2, 3]
  >>> id(l1)
  0x003
  >>> l1 = l1 + [4]
  >>> id(l2)
  0x004
  ```
