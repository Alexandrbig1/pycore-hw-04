def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_dict = {"id": id, "name": name, "age": age}
                cats_info.append(cat_dict)
        return cats_info
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return []
    except Exception as e:
        print(f"Error: An error occurred while processing the file: {e}")
        return []

cats_info = get_cats_info("db_cats.txt")
print(cats_info)
