import RMP

# Test the RMP module
if __name__ == '__main__':
    # Test 1
    print("Test 1")
    professor = RMP.rate_my_prof("Tyler Bletsch")
    professor.retrieveRMPInfo()
    print("Name: %s" % professor.name)
    print("Department: %s" % professor.department)
    print("School: %s" % professor.school)
    print("Rating: %s" % professor.rating)
    print("Difficulty: %s" % professor.difficulty)
    print("Number of Ratings: %s" % professor.num_ratings)
    print("ID: %s" % professor.id)
    print("Would Take Again: %s" % professor.would_take_again)
    for tag, count in professor.tags.items():
            print(f'{tag}: {count} occurrences')
    print("Most recent review: %s" % professor.reviews[0])
