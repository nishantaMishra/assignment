# assignment

[This PDF](CodingQns.pdf) has the questions under consideration.

### Question 1:
If citations are arranged in descending order then 
If the number of elements occurring before the current element is greater than or equal to the value current element, then current element is the h-index of author under consideration. [code](https://github.com/nishantaMishra/assignment/blob/main/h-index-calculator.py)

Example
```bash
Enter the array of citations separated by comma: 1,4,5,8,2,3,1
The researcher\'s h-index is: 3
```

### Question 2
Water will be trapped only if there is atleast one block on either side of any depression. 
This problem could be translated to the problem of counting zeroes. We have to count zeroes lying between two non-zero integers and sequentially remove the last layer of elevation graph. [code](https://github.com/nishantaMishra/assignment/blob/main/water-trap-calculator.py)

Following GIF explains how the algorithm works. It shows if we count only the zeroes occurring in between two non-zero numbers then we will get total amount of water trapped. 1 + 4 + 4 = 9.
![myfile](waterTrapplog.gif)

Example:
```bash

$python3 water-trap-calculator.py
Enter the elevation map: 3,0,1,4,1,1,3,1
Water trapped is: 9 units
```
