---
title: "Boolean Logic Review"
open: false
---

<script>
  import MyImage from '..//images/codecademy_truth_table.png';
</script>



Three if related things:
```
if boolean_value:
elif boolean_value:
else:
```

if `boolean_value` evaluates to True, then what's in the `if boolean_value` statement will run. Then the interpreter will skip to the end of the whole thing  <br>

if `boolean_value` evaluates to False, then what's in the `if boolean_value` statement will not run, and the interpreter will skip what's in the if block and check the next elif. if theres no elif it will run what's in the next else block. if theres no else it will keep going with whatever code is above the else block.  


<br>

OK, but how do we set whether `boolean_value` evaluates to True or False?  

we need to use an expression that evaluates to a boolean (evaluates to True or False)

an expression is made from combining:&nbsp; literals, variables (which evaluate to literals), functions (which evaluate to literals), and operators (which evaluate to literals)

expressions all eventually evaluate to 1 literal value. (eg: 1, 2, 2.0, "Hello", True, False)

a <b>boolean expression</b> is an expression that evaluates to a boolean literal.
Reminder: a boolean is a literal that represents either True or False


Here are the 9 main built in boolean operators that we have learned (<a href="https://www.w3schools.com/python/python_operators.asp">Full list of operators</a>)
We can use these in our boolean expressions:

<pre>
1.&nbsp;&nbsp; a <b> &gt; </b> b &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (returns True if a is greater than b, False otherwise). 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a and b are usually numbers)

2.&nbsp;&nbsp; a <b> &lt; </b> b &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (returns True if a is less than b, False otherwise). 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a and b are usually numbers)

^ there are also &gt;= and &lt;= variants of the above


3.&nbsp;&nbsp; a <b>==</b> b &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (returns True a if is the equivilent value as b, False otherwise).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a and b could be any type of literal)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eg:&nbsp; `1 == 1.0` evaluates to <b>True</b>,&nbsp; `1 == 1.5` evaluates to <b>False</b>.

4.&nbsp;&nbsp; a <b>!=</b> b &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (returns the opposite of a == b) if `a == b` is True, this returns False, 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and vice versa.&nbsp; This is the same thing as saying `not (a == b)`


5.&nbsp;&nbsp; a <b>and</b> b &nbsp;&nbsp;&nbsp;&nbsp; (returns True if a is True and b is True, returns False otherwise).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a and b are both booleans)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eg:&nbsp; `True and False` evaluates to <b>False</b>,&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`True and True` evaluates to <b>True</b>.

6.&nbsp;&nbsp; a <b>or</b> b &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (returns False if both a and b are False, True otherwise).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a and b are both booleans)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(equivalent to ```not( (not a) and (not b) )``` )
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eg:&nbsp; `True or False` evaluates to <b>True</b>,&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`True or True` evaluates to <b>True</b>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`False or False` evaluates to <b>False</b>.

7.&nbsp;&nbsp; <b>not</b> a &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (returns False if a is True, returns True if a is False).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a and b are both booleans)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eg:&nbsp; `not True` evaluates to <b>False</b>,&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`not False` evaluates to <b>True</b>.
</pre>

```Sorry this is broken I copied it over it from another codebase for this site (in which it was done pretty jankily) and I can't be bothered to fix / redo it. ```


<img src="{MyImage}" alt="truth tables" >

<br>

Make sure you understand these.
You can also string these expressions together.
eg: ` (a > 0) and (b > 0) `
this works because `>` is a boolean operator so `a > 0` returns a boolean value, and `and` needs boolean values on both sides to work
If you string to many together it can get confusing, so make sure to use parentheses 


But remember at the end of the day, it all evaluates to one boolean value (True or False), and the place you put the expression, such as an if statement, just sees that value, because the expression will be evaluated before the if statement sees it.
