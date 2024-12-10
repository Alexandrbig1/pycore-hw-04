def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            count = 0
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                count += 1
            if count == 0:
                return (0, 0)
            average_salary = total_salary / count
            return (total_salary, average_salary)
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return (0, 0)
    except Exception as e:
        print(f"Error: An error occurred while processing the file: {e}")
        return (0, 0)


total, average = total_salary("salary_file.txt")
print(f"Total Salary: {total}, Average Salary: {average}")