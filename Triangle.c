Program Triangle 
‘Structured programming version of simple specification
Dim a, b, c As Integer
Dim IsATriangle As Boolean
	‘Step 1: Get Input
Output (“Enter 3 integers which are sides of a triangle”)
Output (a, b, c)
Output (“Side A is”, a)
Output (“side B is”, b)
Output (“side C is”, c)
	‘Step 2: Is A Triangle?
If (a < b + c) AND (b < a + c) AND (c < a+ b)
 	Then IsATriangle = True
 	Else IsATriangle = False
endif
	‘Step 3: Determine Triangle Type
if IsATriangle
	then If (a = b) AND (b = c)
		then Output (“Equilateral”)
 		else If (a ? b) AND (a ? c) AND (b ? c)
 				then Output (“Scalene”)
				else Output (“Isosceles”)
 			 endIf
 		endIf
else Output (“not a Triangle”)
endIf
end triangle2