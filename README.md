# Cient Follow-Up Tracker (CLI Verison)

This Python automation tool helps you track client follow-ups based on the number of days since your last contact. It reads a CSV file of client data and outputs a list of clients who haven't been contacted in a specified number of days.

---

## Features

- Parses client data from a `.csv` file
- Checks how many days since each client was last contacted
- Outputs a follow-up list directly in the terminal
- Optionally saves the results to a new CSV file 

---

## Example 
Enter number of days since last contacted: 7
Clients needing follow-up:

- Jane Doe (jane@example.com) - Last contacted: 2024-12-15 - Notes: Send product demo

Export results to CSV? (y/n):

---


## CSV Format

Your `clients.csv` should be structured like this:

```csv
Name, Email, LastContacted, Notes
Jane Doe, jane@example.comm 2024-12-15, Send product demo
John Smith, john@example.com, 2025-01-10, Interested in package B

## License
MIT License