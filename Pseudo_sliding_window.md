***# SLIDING WINDOW PSEUDO CODE (ALGORITHM FOR DYNAMIC WINDOW):***



Q. Suppose: arr = \[ 2, 5, 1, 7, 10 ], achieve sum K(window) <= 14, with LONGEST SUBARRAY;



left , right = 0;		# Pointers

sum = 0;			# stores sum everycase

max\_len = 0;  			# stores only when max length of subarray encountered



FN.(longest\_arr(arr, K)):



 	while (right < len):

 		sum = sum + arr\[ right ];



 		if (sum <= K):

 			max\_len = max( max\_len, right -left +1 );	# (r-l+1) is length of subarray

 

 		if (sum > K):

 			sum = sum - arr\[ left ]

 			left += 1;



 		right += 1;

 		return(max\_len);





***# BRUTE FORCE:***



FN.(longest\_arr(arr, K)):



 	max\_len = 0;

 	n = len(arr);

 													sub\_array = \[]

 	for ( i=0 --> n-1 ):										#in case elements in longest subarr req:

 		sum = 0;

 		for ( j=i --> n-1 ):									if (sum <= K):

 			sum += lst\[j]										if j-i+1 > max\_len:

 			if (sum >= K):											max\_len = j-i+1

 				max\_len = max(max\_len,sum);								sub\_array = \[i:j+1];

 			else:

 				break;		#optimised

 

 	return max\_len;										return max\_len, sub\_array;





\# ***CONSTANT WINDOW: (SIMPLEST); find maximum sum of 4 numbers*** 



arr = \[--------]

left = 0;

right = K(window) = K;

max\_sum = current\_sum = sum(arr\[ left --> right+1 ]);



while right < len:



&nbsp;	currrent\_sum -= arr\[left];		#removed old left

&nbsp;	left ++;



&nbsp;	right ++;

&nbsp;	current\_sum += arr\[right];		#added new right

&nbsp;	

&nbsp;	max\_sum = max(max\_sum, current\_sum)

&nbsp;	

