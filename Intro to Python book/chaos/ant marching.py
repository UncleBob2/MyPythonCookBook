def marching(lyric):
    print(
        "The little one stops"
        + lyric
        + """
And they all go marching down...
In the ground...
To get out...
Of the rain.
Boom! Boom! Boom!"""
    )


def hurrah(num):
    print("The ants go marching " + num + " by " + num + ", hurrah! hurrah!")
    print("The ants go marching " + num + " by " + num + ", hurrah! hurrah!")
    print("The ants go marching " + num + " by " + num + ",")


my_dic = {
    "one": " to suck his thumb, ",
    "two": " to tie his shoe, ",
    "three": " to drop his stick, ",
    "four": " to comb his hair, ",
}


for key in my_dic:
    hurrah(key)
    marching(my_dic[key])

