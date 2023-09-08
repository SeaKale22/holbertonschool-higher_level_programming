#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    module_names = dir(hidden_4)
    filtered_names = [name for name in module_names if not name.startswith("__")]
    filtered_names.sort()
    for name in filtered_names:
        print(name)
