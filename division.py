import random
import time

def generate_divisible_number(divider):
    while True: #need the while loop to keep generating numbers until you get the right one
        num = random.randint((12*divider), (21*divider))
        if num % divider == 0:
            return num

def main():
    divider = int(input("divisor: "))
    correct_answers = 0
    start_time = time.time()

    while correct_answers < 50:
        num = generate_divisible_number(divider) #calling number
        quotient = num // divider  # Integer division

        while True:
            user_answer = input(f"What is {num} divided by {divider}? ")

            if not user_answer.isdigit(): #if there is a non-numeric input 
                print("Please enter a valid numeric answer.")
            else:
                user_answer = int(user_answer)  # Convert the user's input to an integer

                if (user_answer == quotient):
                    correct_answers += 1
                    print("Correct!\n")
                else:
                    print("Incorrect. Try again.\n")
                
                break #need this so it breaks out of this loop and feeds you a new question
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Congratulations! You solved 50 problems correctly.")
    print(f"Total time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
