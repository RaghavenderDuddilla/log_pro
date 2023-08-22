def search_and_log_error(log_file_paths, search_pattern, error_log_path):
    try:
        with open(error_log_path, 'a') as error_log:
            for log_file_path in log_file_paths:
                try:
                    with open(log_file_path, 'r') as log_file:
                        lines = log_file.readlines()
                    
                    found = False
                    for line in lines:
                        if search_pattern in line:
                            found = True
                            error_log.write(f"Error: Pattern '{search_pattern}' found in '{log_file_path}'\n")
                            print(f"Error logged for pattern in '{log_file_path}'")
                            break
                    
                    if not found:
                        print(f"Pattern not found in '{log_file_path}'")

                except FileNotFoundError:
                    print(f"Log file '{log_file_path}' not found.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    log_file_paths = ["path_to_log_file1.log", "path_to_log_file2.log"]
    search_pattern = "pattern_to_search"
    error_log_path = "error_log.txt"
    
    search_and_log_error(log_file_paths, search_pattern, error_log_path)
