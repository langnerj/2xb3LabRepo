def are_valid_groups(students, groups):
    studentsFromGroups = []
    temp = []
    #extract all group members in a single list
    for i in range(len(groups)):
        if len(groups[i]) == 2 or len(groups[i]) == 3:
            for j in range(len(groups[i])):
                studentsFromGroups.append(groups[i][j])
        else:
            return False
    studentsFromGroups.sort()

    for i in range(len(studentsFromGroups)-1):
        if studentsFromGroups[i+1] == studentsFromGroups[i]:
            return False

    return all(student in studentsFromGroups for student in students)

def test():
    students1 = ["1", "2", "3", "4", "999"]
    students2 = ["1", "2"]
    groups = [["1", "2"], ["4", "5", "6"], ["8", "9"], ["99", "12"]]
    print(are_valid_groups(students1, groups))
    print(are_valid_groups(students2, groups))
test()