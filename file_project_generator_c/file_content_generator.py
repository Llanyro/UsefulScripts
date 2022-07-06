import re


def get_alias_lower(alias: str) -> str:
    alias_list: list = re.findall('[A-Z][^A-Z]*', alias)
    return "_".join([i.lower() for i in alias_list])


def get_formated_file(struct_name: str, alias: str, folders: list, filename: str) -> str:
    result: str = ""
    with open(filename, "r") as f:
        base: str = f.read()
        result = base.format(struct_name.lower(), alias, get_alias_lower(alias), struct_name.upper(), ("_".join(folders)).upper())
    return result


def generate_header(struct_name: str, alias: str, folders: list) -> str:
    return get_formated_file(struct_name, alias, folders, "header.h")


def generate_source(struct_name: str, alias: str, folders: list) -> str:
    return get_formated_file(struct_name, alias, folders, "source.c")


def generate_full(struct_name: str, alias: str, folders: list) -> str:
    return f"{generate_header(struct_name, alias, folders)}" \
           f"\n" \
           f"{generate_source(struct_name, alias, folders)}"


#print(generate_full("CriticalInteger", "CriticalInteger", ["anticheat", "core"]))
