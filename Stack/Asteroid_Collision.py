# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# LEETCODE link: https://leetcode.com/problems/asteroid-collision/description/

def brute_force(asteroids):
    flag = True
    while flag:
        flag = False
        new_lst = []
        i = 0
        while i < len(asteroids):
            if new_lst and new_lst[-1] > 0 and asteroids[i] < 0:
                if new_lst[-1] == -asteroids[i]:
                    new_lst.pop()
                elif new_lst[-1] < -asteroids[i]: # pops a smaller asteroid once at a loop
                    new_lst.pop()
                    new_lst.append(asteroids[i])
                flag = True
            else:
                new_lst.append(asteroids[i])
            i += 1
        asteroids = new_lst # asteroid got updated with list without adjacent smaller asteroid
    return asteroids
    
def optimised(asteroids):
    st = []
    for i in range(len(asteroids)):
        if asteroids[i] > 0:
            st.append(asteroids[i])
        else:
            while st and st[-1] > 0 and st[-1] < -asteroids[i]:
                st.pop()
            if st and st[-1] == -asteroids[i]:
                st.pop()
            elif not st or st[-1] < 0:
                st.append(asteroids[i])
    return st

asteroids = [4,3,1,2,-3,7,-10,3]
print(brute_force(asteroids))
print(optimised(asteroids))