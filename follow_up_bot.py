import csv
import argparse
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# CLI setup
parser = argparse.ArgumentParser(description="Client Follow-Up Automation Tool")
parser.add_argument('--days', type=int, default=7, help="Follow-up with clients who haven't been contacted in X days")
parser.add_argument('--export', action='store_true', help='Export the follow-up results to a CSV file')
args = parser.parse_args()

# Read client data from CSV file
clients_to_follow_up = []
today = datetime.now()

try:
    with open(args.file, mode="r", newline='') as file:
        reader = csv.DictReader(file)

        print(Fore.CYAN + f"\n[+] Scanning for clients needing follow-up(>{args.days} days)...\n")

        for row in reader:
            name = row['Name']
            email = row['Email']
            notes = row['Notes']
            last_contacted = datetime.strptime(row['LastContacted'], "%Y-%m-%d")
            days_since_contacted = (today - last_contacted).days

            if days_since_contacted > args.days:
                clients_to_follow_up.append({
                    'Name': name,
                    'Email': email,
                    'Last Contacted': last_contacted.strftime("%B %d, %Y"),
                    'Days Since Last Contact': days_since_contacted,
                    'Notes': notes
                })
except FileNotFoundError:
    print(Fore.RED + f"[!] Error: File '{args.file}' not found.")
    exit()
except Exception as e:
    print(Fore.RED + f"[!] An unexpected error occurred: {e}")
    exit()

except FileNotFoundError:
    print(Fore.RED + f"[!] Error: File '{args.file}' not found.")
    exit()

# Display results
if clients_to_follow_up:
    for client in clients_to_follow_up:
        print(Fore.GREEN + f"- {client['Name']} ({client['Email']})")
        print(Fore.Yellow + f" Last Contacted: {client['Last Contacted']}")
        print(Fore.MAGENTA + f" Days Since: {client['Days Since Last Contact']}")
        print(Fore.CYAN + f" Notes: {client['Notes']}\n")

    print(Fore.BLUE + f"[+] Total: {len(clients_to_follow_up)} clients need follow-up.\n")

    # Export to CSV
    if args.export:
        with open("follow_up_clients.csv", mode="w", newline='') as output:
            fieldnames = ['Name', 'Email', 'Last Contacted', 'Days Since Last Contact', 'Notes']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            for client in clients_to_follow_up:
                writer.writerow(client)
        print(Fore.GREEN + "[+] Exported to 'follow_up_results.csv' successfully.")

else:
    print(Fore.RED + "[!] No clients need follow-up today.")