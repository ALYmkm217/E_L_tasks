
import webbrowser

# Dictionary of favorite websites with names as keys and URLs as values
favorite_websites = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "GitHub": "https://www.github.com",
}

def print_menu():
    print("Favorite Websites:")
    for index, site_name in enumerate(favorite_websites.keys(), start=1):
        print(f"{index}. {site_name}")

def open_website(url):
    webbrowser.open(url)  

if __name__ == "__main__":
    while True:
        print_menu()
        choice = int(input("Enter the number of the website you want to visit (0 to exit): "))
        
        if choice == 0:
            print("Exiting...")
            break  # Exit the loop if the user chooses to exit
        
        site_names = list(favorite_websites.keys())
        
        if 1 <= choice <= len(site_names):
            chosen_site_name = site_names[choice - 1]
            chosen_site_url = favorite_websites[chosen_site_name]

            print(f"Opening {chosen_site_name}...")
            open_website(chosen_site_url)
        else:
            print("Invalid choice. Please select a valid number.")

