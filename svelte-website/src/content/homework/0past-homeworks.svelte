<script>
	import Bubble from "$lib/Bubble.svelte";

	import truth_table from "../images/codecademy_truth_table.png"
	import factorial_function from "../images/factorial_function.png"
	import fizzbuzz from "../images/fizzbuzz.png"
	import fnexcercise from "../images/fnexcercise.png"
	import forloopsrecap from "../images/for_loops_lesson_recap.png"
	import python_if_1 from "../images/python-if-image-1.png"
	import python_problem_2 from "../images/python-problem-2.png"

</script>


<Bubble title="Lesson 2 Homework">
	<p>
		1.&nbsp; Please do the quiz linked at the bottom of <a href="https://www.py4e.com/lessons/logic"> this page</a>.
	</p>

	<p> 
		2.&nbsp; Please do 
		<a href="https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true">this problem</a> 
		on HackerRank. 
		(You will need to make an account sorry).
	</p>
	<p style="margin-top:5px;">
		Write all your code inside of the provided if statement block (under
		<code>if __name__ == main:</code>)
	</p>
	<p>
		<u>Optional extra homework:</u>&nbsp; feel free to do the next hackerrank challenge after you are done with the one linked above. (It should be the one called "Arithmetic Operations")
	</p>
</Bubble>


<Bubble title="Lesson 3 Homework (More if practice)">
	<p>
		1.&nbsp; Please solve the following Problem completely on your own:
	</p>
	<img src={python_if_1} alt="">
	<p>
		2.&nbsp; Extra Credit:
	</p>
	<img src={python_problem_2} alt="" style="width:70%">
</Bubble>


<Bubble title="Lesson 4 Homework (Functions, arguments and return)">
	<p>
		Please do all of the following:
	</p>
	<p>
		1.&nbsp; Please solve 
		<a href="https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true">this</a>
		HackerRank problem relating to writing a function and if statements 
	</p>
	<p>
		2.&nbsp; Please solve 
		<a href="https://codingbat.com/prob/p194053">this</a>
		codingbat challenge (hint: built in `len()` function returns length of a string),
	</p>
	<p>
		3.&nbsp; Please solve this:
		<a href="https://codingbat.com/prob/p162058">this</a>
		codingbat challenge
	</p>
	<p style="margin-bottom:5px">
		4.&nbsp; do the following exercise from the slides:
	</p>
	<img src={fnexcercise} alt="" style="width:70%">

	<p style="margin-bottom:5px">
		5.&nbsp; <s>Extra Credit</s> No longer Extra Credit:
	</p>
	<img src={factorial_function} alt="">
	<details class="no-box" style="margin-left:35px">
		<summary style="margin-left:-35px"> Hint </summary>
		you can call functions recursively, meaning you can call the function you are currently in from within itself
	</details>

	<p style="margin-bottom:5px">
		6.&nbsp; Extra Credit: do <a href="https://codingbat.com/prob/p162058">this</a> coding bat challenge in 1 line of code. 
		Read the section below this to help you out. 
		
	</p>
	<p style="margin-top:5px;">
		Hint: they already got it down to 3 lines right?, 
		how could you use the same strategy as them to do it in 1 line (return a boolean directly that is derrived from a boolean expression made using ands/ors )
	</p>
</Bubble>


<Bubble title="Lesson 6-ish Homework (While loops)">
	<p>
		Please do all of the following:
	</p>
	
	<p style="margin-bottom:5px">
		1.&nbsp; Please solve 
		<a href="https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true">this</a>
		HackerRank problem.
		
	</p>
	<p style="margin-bottom:5px; margin-top:5px;">
		Two facts that may or may not come in handy: 
	</p>
	<p style="margin-bottom:10px; margin-top:10px; margin-left:20px;">
		1)&nbsp; ``` my_string_var += "something" ``` is shorthand for ```my_string_var = my_string_var + "something" ``` and can help you build up a string
	</p>
	<p style="margin-bottom:5px; margin-top:5px; margin-left:20px;">
		2)&nbsp; ``` print("some text", end="") ``` will print to the console without making a new line
	</p>

	<!-- <p style="margin-bottom:5px">
		2.&nbsp;
		fizzbuzz (I will save for later for for loops)
	</p> -->
	
	<p style="margin-bottom:5px">
		2.&nbsp;
		Write a function that takes in a number as a parameter and returns the factorial of the number. The function should have a while loop inside it and is not allowed to call itself
	</p>
	<p style="margin-bottom:5px; margin-top:5px;">
		Tips: 1) look at slides for example of how they use while loop. 2) if you need to debug your code put print statements in the while loop that print out each of the variables (eg `print(x,y,z)`), so you can follow in your head what code is run when and how all the values are changing
	</p>

	<p style="margin-bottom:5px">
		3.&nbsp; Extra Credit:
		Get 100% on  
		<a href="https://www.khanacademy.org/computing/computer-programming/programming/looping/e/review-loops">this quiz about while loops</a>.
		(it's written in javascript though)
	</p>
</Bubble>

<!-- <Bubble title="Lesson 7 & 8 Homework (for loops + string indexing) -- IGNORE FOR NOW">
	<p>
		1. &nbsp; Make yet another function to calculate the factorial, this time using for loops instead of while loops. 
		Also try to use good variable names if you can.
	</p>
	
	<p>
		2. &nbsp; Do 
		<a href="https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true"> this</a>
		hackerrank problem.
	</p>
	<p style="margin-top:10px;margin-left: 40px;">
		This one is a bit hard, but you can do it using what we've learned so far (see class recap screenshot at top of page): namely using for loop and string slicing (the thing with string_var[start:end:step]). of course you can use variables inside the brackets
	</p>
	<p style="margin-top:10px; margin-left: 40px;">Tips:</p>
	
	<div style="margin-top:0px; margin-left: 45px; border-left: 1px solid black; padding-left: 40px">
		<p style="margin-top:5px;">
			- print statements. Print what is going on at each stage of the loop, print what variables are and see if they are what you'd expect.
		</p>
		<p style="margin-top:5px; margin-left: 70px;">
			- However once you're ready to submit comment out the print statements so hackerrank accepts it
		</p>
		<p style="margin-top:10px;">
			- use pointless variables (with good names): ie if a line of code gets to complicated then you can extract parts of it into named variables. This way you can edit each part of it separately and also test each part is what you would expect by printing it.
		</p>
	</div>
	<p style="margin-top:15px; margin-left: 40px;">
		try your best if you don't succeed we'll go over it in class
	</p>

	<p>
		3. &nbsp; Extra Credit: Do 3 or more 
		<a href="https://codingbat.com/python">codingbat</a>
		problems from any section other than warmup
	</p>

	<p>
		4. Fizzbuzz is a classic coding challenge problem that is pretty simple and is used to verify if someone even knows the basics of how to code, and to see how they think about optimizing their code. The homework assignment is just to complete it correctly.
	</p>
	<img src={fizzbuzz} alt="">

</Bubble> -->

<style>
	p {
		margin: 24px 0;
	}
</style>