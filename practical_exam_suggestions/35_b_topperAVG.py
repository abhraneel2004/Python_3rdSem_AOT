def sub_avg(marks):
    l = []
    print("Subject Average: ")
    for j in range(6):
        sum = 0
        for i in range(5):

            m = marks[i][j]

            sum += m

        print(f"Subject {j+1}: {sum/5}")


def topper_avg(marks):
    max = marks[0]
    for i in range(len(marks)):

        if sum(marks[i]) > sum(max):
            max = marks[i]
    print("Topper Average: ", sum(max)/6)


marks = []
for i in range(5):
    print(f"Enter the marks of student {i+1}: ")
    l = []
    for j in range(6):
        try:
            l.append(int(input(f"Subject {j+1}: ")))
        except:
            l.append(0)

    marks.append(l)


# marks = [[4,5,3,5,6,3],[5,4,5,4,3,6],[4,5,3,6,4,4],[5,4,6,6,4,5],[6,4,6,6,4,6]]
sub_avg(marks)
topper_avg(marks)
