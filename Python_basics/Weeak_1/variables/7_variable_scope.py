#Local vs Global Variables
# Global variables
global_counter = 0
company_name = "Tech Corp"

def update_counter():
    # Local variable
    local_count = 10
    # Modifying global variable
    global global_counter
    global_counter += 1
    
    print(f"Local count: {local_count}")
    print(f"Global counter: {global_counter}")

def display_company():
    print(f"Company: {company_name}")

# Test the functions
update_counter()
display_company()
# print(local_count)  # This would cause an error - local_count is not accessible hereme}")me}")