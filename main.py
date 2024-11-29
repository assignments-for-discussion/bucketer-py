
def count_batteries_by_health(present_capacities):
  #classifying batteries based on their state of health
  #intialize
  healthy_count = 0
  exchange_count = 0
  failed_count = 0

  rated_capacity = 120 # rated capacity of the new battery given

  #classify battries based on state of health for thier present capacity
  # to calculate state if health percentage using the formula provided 
  for capacity in present_capacities:
    soh_percentage = (capacity/rated_capacity)*100
    #classify the soh ranges 
    if soh_percentage>80: 
      healthy_count = healthy_count+1
    elif 62<=soh_percentage<=80:
      exchange_count = exchange_count+1
    else:
      failed_count = failed_count+1

  return{
    "healthy": healthy_count,
    "exchange": exchange_count,
    "failed": failed_count
    }

def test_bucketing_by_health():
  
  print("Counting batteries by SoH...\n")   #testing the battery classification function
  
  present_capacities = [113, 116, 80, 95, 92, 70]  #testing data provided
  
  counts = count_batteries_by_health(present_capacities) # running the function on the given data
  print("The count for the data provided") # just printing the values 
  print(counts)
  #asserting the values to check if they are right or wrong
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)

  # adding additional test cases to check all the edge cases as well 
  additional_test_data = [120,62,61]
  additional_count = count_batteries_by_health(additional_test_data)
  print("The count for the additional data provided") # just printing the values 
  print(additional_count)
  #asserting the values 
  assert(additional_count["healthy"] == 1)
  assert(additional_count["exchange"] == 0)
  assert(additional_count["failed"] == 2)
  #Once the testing is done it will display a message
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
