
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import apis

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("step 1: Creating machines a,b,c of type 1 and machine d of type 2, "
          "using 'create_machine' function")
    apis.create_machine("a", "1")
    apis.create_machine("b", "1")
    apis.create_machine("c", "1")
    apis.create_machine("d", "2")
    print("step 2: Getting machines name list using 'get_machines_names' function:")
    print(apis.get_machines_names())

    print("step 3: Time T0- starting machines a,b,c,d")
    apis.start_machine("a")
    apis.start_machine("b")
    apis.start_machine("c")
    apis.start_machine("d")
    print("Waiting for 60 seconds")
    time.sleep(60)

    print("step 4: After 60 seconds from T0, time T1- creating and starting machine e of type 2")
    apis.create_machine("e", "2")
    apis.start_machine("e")
    print("Waiting for 60 seconds")
    time.sleep(60)

    print("step 5: After 60 seconds from T1, time T2- machine b went down")
    apis.stop_machine("b")
    print("Waiting for 60 seconds")
    time.sleep(60)

    print("Cost per type of machine : get_machine_cost per min in $:")
    print("a", apis.get_machine_cost("a"))
    print("b", apis.get_machine_cost("b"))
    print("c", apis.get_machine_cost("c"))
    print("d", apis.get_machine_cost("d"))
    print("e", apis.get_machine_cost("e"))

    print("step 6: After 60 seconds from T2- getting the prices for each machine")

    print("Cost per machine: get_total_cost_per_machine_name (in $ per min):")
    print(apis.get_total_cost_per_machine_name())

    print("Total cost of all machines together (in $ per min): get_total_cost")
    print(apis.get_total_cost())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
