"""A very large variance means that the students' grades were all over the place, while a small variance (relatively close to the average) means that the majority of the students had similar grades.
The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.
"""


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  variance = variance / len(scores)
  return variance

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print "grades: " + str(grades)
print "suma of grades: " + grades_sum(grades)
print "average grade: " + grades_average(grades)
print "variance: " + grades_variance(grades)
print "standard deviation: " + grades_std_deviation(variance)