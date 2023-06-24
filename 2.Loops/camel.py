name = input("camelCase: ")
import pdb


# name = "FaizX"

# faz = name.isalpha()
# print(faz) 
final_name = ""
for _ in name:
    # print(_)
    name1 = _.isupper()
    # print(name1)
    if name1 is True:
        # print("alph")
        _ = _.swapcase()
        # print(f"{name1} + ok ")
        _ = "_" + _
        # print(_)
        # pdb.set_trace()
    final_name += _
    # pdb.set_trace()
    # print("of")
    # if _ is True:
    #     print("hello")



print(f"snake_case: {final_name}")
"""
swapcase
"""


#variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, 
#and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.



"""
This codespace is currently running in recovery mode due to a container error.
1. Use Cmd/Ctrl + Shift + P -> "Codespaces: View Creation Log" to see full logs
2. Update your devcontainer configuration as needed
3. Use Cmd/Ctrl + Shift + P -> "Codespaces: Rebuild Container" to retry
4. For help, read more about custom configuration: https://aka.ms/ghcs-custom-configuration
@mohdfaizan3 ➜ /workspaces/79694828 (main ✗) $ 
"""