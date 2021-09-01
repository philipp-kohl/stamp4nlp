import os

import yaml

roles_path = "{{cookiecutter.project_folder}}/docs/source/_data/roles"
tasks_path = "{{cookiecutter.project_folder}}/docs/source/_data/tasks"


def main():
    print("Reading Files")
    roles = os.listdir(roles_path)
    tasks = os.listdir(tasks_path)

    roles_information = load_roles(roles)
    tasks_information = load_tasks(tasks)

    print("Extract Information")
    roles_information = extract_additional_performing_tasks_for_roles(roles_information, tasks_information)

    print("Writing Files")
    save_roles(roles_information)


def load_roles(roles):
    roles_information = {}
    for role in roles:
        with open(roles_path + "/" + role, "r") as file:
            role_dict = yaml.safe_load(file)
            role_dict["tmp_file_name"] = role
            roles_information[role_dict["name"]] = role_dict

    return roles_information


def load_tasks(tasks):
    tasks_information = {}
    for task in tasks:
        with open(tasks_path + "/" + task, "r") as file:
            task_dict = yaml.safe_load(file)
            tasks_information[task_dict["name"]] = task_dict

    return tasks_information


def extract_additional_performing_tasks_for_roles(roles_information, tasks_information):
    for role in roles_information:
        extract_additional_performing_tasks_for_role(role, roles_information, tasks_information)

    return roles_information


def extract_additional_performing_tasks_for_role(role, roles_information, tasks_information):
    additional_performing_tasks = []
    for task in tasks_information:
        if "additional_roles" in tasks_information[task]:
            if role in tasks_information[task]["additional_roles"]:
                additional_performing_tasks.append(tasks_information[task]["name"])
    # Now filter all responsible tasks. Otherwise some tasks appear twice.
    roles_information[role]["performs"] = [task for task in additional_performing_tasks if
                                           task not in roles_information[role].get("responsible_for", [])]


def save_roles(roles_information):
    for role in roles_information:
        file_name = roles_information[role]["tmp_file_name"]
        del roles_information[role]["tmp_file_name"]
        with open(roles_path + "/" + file_name, "w") as file:
            yaml.dump(roles_information[role], file)


if __name__ == "__main__":
    print("Begin Generation")
    main()
    print("End Generation")

