import random 
import string

def get_user_input():
    department = input("Enter the department name: ")
    num_instances = int(input("Enter the number of EC2 instances: "))
    return department, num_instances

def generate_random_string(length=6):
    letters = string.ascii_uppercase
    digits = string.digits
    random_string = ''.join(random.choice(letters + digits) for _ in range(length))
    return random_string

def generate_ec2_names(department, num_instances):
    ec2_names = []
    for _ in range(num_instances):
        random_string = generate_random_string()
        ec2_name = f"{department}-{random_string}"
        ec2_names.append(ec2_name)
    return ec2_names

def print_ec2_names(ec2_names):
    print("\nGenerated EC2 Names:")
    for name in ec2_names:
        print(name)

def main():
    department, num_instances = get_user_input()
    ec2_names = generate_ec2_names(department, num_instances)
    print_ec2_names(ec2_names)

if __name__ == "__main__":
    main()
