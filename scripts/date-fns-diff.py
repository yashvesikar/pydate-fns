# function to convert camelCase string to snake_case
def camel_to_snake(name):
    import re

    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


if __name__ == "__main__":
    import os

    # from pprint import pprint as print

    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pydate"))
    # print list all directories in current directory
    pydate_methods = [i for i in os.listdir() if os.path.isdir(i)]

    # reset path to current script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # navigate to sibling directory
    os.chdir(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            "date-fns",
            "src",
        )
    )
    # print list all directories in current directory
    date_fns_methods = [camel_to_snake(i) for i in os.listdir() if os.path.isdir(i)]

    # print a text table with 3 columns, left aligned, 30 chars wide: method, pydate, date-fns
    print("method".ljust(60), "pydate".ljust(10), "date-fns".ljust(10))
    print("-" * 90)
    for method in sorted(date_fns_methods):
        print(
            method.ljust(60),
            str((method in pydate_methods) or "").ljust(10),
            str(method in date_fns_methods).ljust(10),
        )
