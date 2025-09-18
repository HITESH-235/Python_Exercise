# ______________________________________________________Procedure Explained:________________________________________________

# CHECK_ITH_BIT: (AND)
# 1.Left Shifts:
#   do ((num & mask) != 0)
#   e.g. num="1100"; i=2; mask="0100"; 
# 2.Righ Shifts: (&)
#   do ((num>>i) & 1 != 0)
#   rightshifting num by i brings the ith digits to front to be checked by 1, through &;
#   if 0; then ith bit is not set; else it is set
# __________________________________________________________________________________________________________________________

# TOGGLE_ITH_BIT: (XOR)
# * (num ^ mask) is res *
# 1.if both (num and mask)'s ind are same: 0 is added;
#   hence if num and mask are 0 then "remains" 0
#   if num and mask are 1 then "changes" to 0

# 2.if both are opposite: 1 is added;
#   if num has 1 and mask has 0; then "remains" 0
#   if num has 0 and mask has 1; then "changes" to 0
# __________________________________________________________________________________________________________________________

# REMOVE_ITH_BIT: (N AND N-1)
# 1.(n-1) has all 0s inverted before first 1 encountered from right in n
#   rest part of n-1 is same as n
#   hence the first 1 from right, using n & n-1, toggles when n -> 1 and (n-1) -> 0
# 2.e.g. n = 10100 then n-1 = 10011; hence (10100 & 10011) = 10000 (2nd index 1 was removed)
# __________________________________________________________________________________________________________________________


# CHECKing if ith bit from a number is SET or not: return True or False
def check_ith_L_Shift(num, i):
    mask = 1 << i
    return num & mask != 0

def check_ith_R_Shift(num, i):
    return (num>>i) & 1 != 0


# TOGGLE the ith bit of num: return the num
def toggle_ith(num,i):
    mask = 1 << i
    return bin(num ^ mask)


# REMOVE the last set bit: return num (AND)
def remove_ith(num):
    return bin(num & num-1)
num = 20
print(remove_ith(20))