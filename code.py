def are_valid_groups(students, groups):
    studentsFromGroups = []
    #extract all group members in a single list
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            studentsFromGroups.append(groups[i][j])

    return all(student in studentsFromGroups for student in students)

def test():
    students1 = [1, 2, 3, 4, 999]
    students2 = [1, 2]

    groups = [[1, 2], [3], [4, 5, 6], [7, 9], [99, 12]]
    print(are_valid_groups(students1, groups))
    print(are_valid_groups(students2, groups))

test()