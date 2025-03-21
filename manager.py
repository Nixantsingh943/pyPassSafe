import os
import json
import getpass
from cryptography.fernet import Fernet
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode())


def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()


def save_password(service, username, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    data = {service: {"username": username, "password": encrypted_password.decode()}}

    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                passwords = json.load(file)
            except json.JSONDecodeError:
                passwords = {}
        passwords.update(data)
    else:
        passwords = data

    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

    console.print(f"[bold green]✅ Password saved for [cyan]{service}[/cyan]![/bold green]")


def list_services():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                passwords = json.load(file)
            except json.JSONDecodeError:
                console.print("[bold red]⚠ Error: Password file is corrupted![/bold red]")
                return

        if passwords:
            table = Table(title="🔐 Stored Services", show_header=True, header_style="bold magenta")
            table.add_column("Service", style="cyan", justify="left")
            table.add_column("Username", style="yellow", justify="left")

            for service, creds in passwords.items():
                table.add_row(service, creds["username"])

            console.print(table)
        else:
            console.print("[bold yellow]⚠ No services found![/bold yellow]")
    else:
        console.print("[bold yellow]⚠ No password file found![/bold yellow]")


def retrieve_password(service):
    key = load_key()
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                passwords = json.load(file)
            except json.JSONDecodeError:
                console.print("[bold red]⚠ Error: Password file is corrupted![/bold red]")
                return None, None

        if service in passwords:
            encrypted_password = passwords[service]["password"]
            decrypted_password = decrypt_password(encrypted_password.encode(), key)
            return passwords[service]["username"], decrypted_password
        else:
            console.print("[bold red]❌ Service not found![/bold red]")
            return None, None
    else:
        console.print("[bold red]⚠ No stored passwords found![/bold red]")
        return None, None


def main():
    if not os.path.exists("secret.key"):
        generate_key()

    while True:
        console.print("\n[bold cyan]🔒 Password Manager[/bold cyan]", style="bold underline")
        console.print("[bold green]1.[/bold green] 🔑 [green]Save a new password[/green]")
        console.print("[bold yellow]2.[/bold yellow] 🔍 [yellow]Retrieve an existing password[/yellow]")
        console.print("[bold blue]3.[/bold blue] 📜 [blue]List stored services[/blue]")
        console.print("[bold red]4.[/bold red] ❌ [red]Exit[/red]")

        choice = Prompt.ask("\n[bold magenta]👉 Enter your choice[/bold magenta]", choices=["1", "2", "3", "4"])

        if choice == "1":
            service = Prompt.ask("[bold cyan]📌 Enter service name[/bold cyan]")
            username = Prompt.ask("[bold cyan]👤 Enter username[/bold cyan]")
            password = getpass.getpass("🔑 Enter password: ")
            save_password(service, username, password)

        elif choice == "2":
            list_services()
            service = Prompt.ask("[bold yellow]🔍 Enter service name to retrieve[/bold yellow]")
            username, password = retrieve_password(service)
            if username:
                console.print("\n[bold green]🔓 Retrieved Credentials:[/bold green]")
                console.print(f"📌 Service: [cyan]{service}[/cyan]")
                console.print(f"👤 Username: [yellow]{username}[/yellow]")
                console.print(f"🔑 Password: [red]{password}[/red]")

        elif choice == "3":
            list_services()

        elif choice == "4":
            console.print("[bold red]👋 Exiting... Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main()
