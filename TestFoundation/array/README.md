**This folder is for testing the method on separating array until the last index by separate into pair and sum it up**
**For example** , 
array = [ 1 , 2 , 3 , 4, 5, 6]
Then, we will separate into smaller group **[1 ,2 ] , [3 , 4] , [5,6] **
After that we will get:
* 1+2 = 3
* 3+4=7
* 5+6 = 11
  Therefore, there will be another array **[3,7,11]**
  After that, we notice there is 3 items which is odd.

<h3>**How do we solve this?**</h3>
<h4>**The issue of the problem of odd nums**</h4>
* It hard to sum it up and have 1 index in the array unlike there is even numbers which can divide into pairs equally.
**The way we can solve this odd nums**
* We need to get rid of the last index and store into another variable for future use
* Then, we can use called out the function that we created which is called separation() function for breaking the array down into smaller pair
* Then, the process of the function will be the same step as above and we add the end index to the array

Therefore, we will get from **[A,B,C] to [X,C]** by **A+B=X**; After that we will return the **_array[0] + array[1]_**

**_In this file we will use 2 array: The original array as an input. Another array is for output and reuse within the function_**

**In this method, we will reuse the array by we using 2 arrays and recall over again until there is one index left**
