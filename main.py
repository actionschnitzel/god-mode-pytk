#!/usr/bin/python3

# sudo apt install python3-tk


from tkinter import *
import tkinter as tk
from os import popen
import subprocess
import os

# import distro


def gimme_term():
    popen("x-terminal-emulator")


def get_linux_distribution_etc_os_release():
    try:
        distribution_info = {}
        with open("/etc/os-release", "r") as os_release:
            for line in os_release:
                key, value = map(str.strip, line.strip().split("=", 1))
                distribution_info[key] = value.strip('"')

        return distribution_info
    except FileNotFoundError:
        return None


global distribution_info
distribution_info = get_linux_distribution_etc_os_release()


def check_nvidia_gpu():
    try:
        # Run 'lspci' command to list PCI devices and pipe the output to grep
        result = subprocess.check_output(["lspci | grep NVIDIA"], shell=True, text=True)

        # Check if the result contains "NVIDIA Corporation" (indicating an NVIDIA GPU)
        if "NVIDIA Corporation" in result:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print("Error running 'lspci' command:", e)
        return False


def is_wine_installed():
    try:
        # Run the 'wine --version' command and capture the output
        subprocess.check_output(["wine", "--version"], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False


def get_linux_distribution():
    try:
        with open("/etc/os-release", "r") as os_release:
            for line in os_release:
                if line.startswith("ID="):
                    _, distribution = line.strip().split("=")
                    return distribution.lower()
    except FileNotFoundError:
        pass
    return None


distro = get_linux_distribution()


def check_debian_release():
    try:
        with open("/etc/os-release", "r") as os_release_file:
            id_like_debian = False
            debian_codename = False

            for line in os_release_file:
                if line.startswith("ID_LIKE=debian"):
                    id_like_debian = True

                if line.startswith("DEBIAN_CODENAME="):
                    debian_codename = True

            return id_like_debian and debian_codename
    except FileNotFoundError:
        return False


def check_ubuntu_release():
    try:
        with open("/etc/os-release", "r") as os_release_file:
            id_like_debian = False
            debian_codename = False

            for line in os_release_file:
                if line.startswith("ID_LIKE=ubuntu"):
                    id_like_debian = True

            return id_like_debian and debian_codename
    except FileNotFoundError:
        return False


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        """defines the basic look of the app"""
        # Window Basics
        self.title("G.O.D-Mode -- Gaming On Debian 23.10")
        self.resizable(0, 0)

        app_width = 590
        app_height = 650
        global screen_width
        screen_width = self.winfo_screenwidth()
        global screen_height
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.brave_icon = PhotoImage(file="icons/cute_tux.png")

        def nvidia_top():
            nd_le = Nvidia_Top(self)
            nd_le.grab_set()

        def wine_top():
            wine_le = Wine_Top(self)
            wine_le.grab_set()

        def lutris_top():
            lutris_le = Lutris_Top(self)
            lutris_le.grab_set()

        def heroic_top():
            heroic_le = Heroic_Top(self)
            heroic_le.grab_set()

        def steam_top():
            steam_le = Steam_Top(self)
            steam_le.grab_set()

        # Path to the /bin/flatpak file
        flatpak_path = "/bin/flatpak"
        lutris_directory = os.path.expanduser("~/.local/share/lutris")
        desktop_launcher_path = os.path.expanduser(
            "~/.local/share/applications/steam.desktop"
        )
        heroic_path = os.path.expanduser("~/.var/app/com.heroicgameslauncher.hgl")
        # Get the current working directory
        global current_directory
        current_directory = os.getcwd()

        self.main_frame = Frame(self, padx=20, pady=20, background="#09928B")
        self.main_frame.pack(fill="both", expand=TRUE)

        self.hadder = Label(
            self.main_frame,
            compound=TOP,
            text="Not Your Mommy Edition (Learn Terminal!)",
            image=self.brave_icon,
            background="#09928B",
            foreground="#FFFFFF",
        )
        self.hadder.pack()

        self.syscore = LabelFrame(
            self.main_frame,
            text="System CheckUp",
            font=("Sans", 12),
            padx=20,
            pady=20,
            background="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
        )
        self.syscore.pack(pady=10, fill="x")

        self.your_distro = Label(self.syscore, background="#FFFFFF")
        self.your_distro.pack(anchor=W)

        self.your_distro_full = Label(self.syscore, background="#FFFFFF")
        self.your_distro_full.pack(anchor=W)

        self.distro_id = Label(self.syscore, background="#FFFFFF")
        self.distro_id.pack(anchor=W)

        self.graka = Label(self.syscore, background="#FFFFFF")
        self.graka.pack(anchor=W)

        self.wine_i = Label(self.syscore, background="#FFFFFF")
        self.wine_i.pack(anchor=W)

        self.flat_i = Label(self.syscore, background="#FFFFFF")
        self.flat_i.pack(anchor=W)

        self.steam_i = Label(self.syscore, background="#FFFFFF")
        self.steam_i.pack(anchor=W)

        self.lutris_i = Label(self.syscore, background="#FFFFFF")
        self.lutris_i.pack(anchor=W)

        self.heroic_i = Label(self.syscore, background="#FFFFFF")
        self.heroic_i.pack(anchor=W)

        self.surface_core = LabelFrame(
            self.main_frame,
            text="Installers",
            font=("Sans", 12),
            pady=5,
            padx=5,
            background="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
        )
        self.surface_core.pack(pady=10, fill="x")

        def surf_action(text):
            """Passes commands du auto generated buttons"""
            if text == "Nvidia Driver":
                nvidia_top()
            if text == "Wine":
                wine_top()
            if text == "Flatpak Support":
                popen("xdg-open https://flathub.org/setup")
            if text == "Lutris":
                lutris_top()
            if text == "Heroic":
                heroic_top()
            if text == "Steam":
                steam_top()

        # Button list
        surface_button_list = [
            "Nvidia Driver",
            "Flatpak Support",
            "Wine",
            "Steam",
            "Lutris",
            "Heroic",
        ]

        surface_button_list1 = []
        conf_row = 0
        conf_column = 0
        for surf_button in surface_button_list:
            # Generates buttons from list with grid
            self.surface_button_x = Button(
                self.surface_core,
                width=18,
                text=surf_button,
                command=lambda text=surf_button: surf_action(text),
                borderwidth=0,
                highlightthickness=0,
            )
            self.surface_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            surface_button_list1.append(self.surface_button_x)
            conf_column = conf_column + 1
            if conf_column == 3:
                conf_row = conf_row + 1
                conf_column = 0
            if surf_button == "Heroic" and os.path.exists(flatpak_path) == False:
                print("Bla")
                # self.surface_button_x.config(state=DISABLED)
            if surf_button == "Wine" and is_wine_installed() == True:
                print("Bla")
                # self.surface_button_x.config(state=DISABLED)
            if surf_button == "Lutris" and os.path.exists(lutris_directory) == True:
                print("Bla")
                # self.surface_button_x.config(state=DISABLED)
            if surf_button == "Steam" and os.path.exists(desktop_launcher_path) == True:
                print("Bla")
                # self.surface_button_x.config(state=DISABLED)
            if (
                surf_button == "Flatpak Support"
                and os.path.exists(flatpak_path) == True
            ):
                print("Bla")
                # self.surface_button_x.config(state=DISABLED)
            if surf_button == "Nvidia Driver" and check_nvidia_gpu() == False:
                print("Bla")
                # self.surface_button_x.config(state=DISABLED)

        if os.path.exists(desktop_launcher_path):
            print("Steam is installed")
            self.steam_i.configure(text="Steam: Installed")
        else:
            print("Steam is not installed")
            self.steam_i.configure(text="Steam: Not Installed")

        if distribution_info:
            print(f"PRETTY_NAME: {distribution_info.get('PRETTY_NAME', 'N/A')}")
            print(f"DEBIAN_CODENAME: {distribution_info.get('DEBIAN_CODENAME', 'N/A')}")
            self.your_distro.configure(
                text=f"Debian Codename: {distribution_info.get('DEBIAN_CODENAME', 'N/A')}"
            )
            self.your_distro_full.configure(
                text=f"Full Name: {distribution_info.get('PRETTY_NAME', 'N/A')}"
            )

            distro_id = distribution_info.get("ID", "").lower()
            if distro_id in ["debian", "ubuntu", "linuxmint", "lmde", "pop"]:
                print(
                    f"Your Linux distribution is based on Debian: {distro_id.capitalize()}"
                )
            else:
                print("Your Linux distribution is not based on Debian.")
        else:
            print("Unable to determine Linux distribution information.")

        if is_wine_installed():
            print("Wine is installed on this system.")
            self.wine_i.configure(text="Wine: Installed")
        else:
            print("Wine is not installed on this system")
            self.wine_i.configure(text="Wine: Not Installed")

        if os.path.exists(lutris_directory):
            print(f"Lutris is installed.")
            self.lutris_i.configure(text=f"Lutris: Installed")
        else:
            print(f"Lutris is not installed.")
            self.lutris_i.configure(text=f"Lutris: Not Installed (Needs Flatpak)")

        # Check if the directory exists
        if os.path.exists(heroic_path):
            print(f"Heroic is installed.")
            self.heroic_i.configure(text=f"Heroic Games Launcher: Installed")
        else:
            print(f"Heroic is not installed.")
            self.heroic_i.configure(
                text=f"Heroic Games Launcher: Not Installed (Needs Flatpak)"
            )

        # Check if the file exists
        if os.path.exists(flatpak_path):
            print(f"Flatpak is installed.")
            self.flat_i.configure(text=f"Flatpak Support: Installed")
        else:
            print(f"Flatpak is not installed.")
            self.flat_i.configure(text=f"Flatpak Support: Not Installed")

        if check_nvidia_gpu():
            print("You are using an NVIDIA graphics card.")
            self.graka.configure(text="Driver: You are using an NVIDIA graphics card")
        else:
            print("You are not using an NVIDIA graphics card.")
            self.graka.configure(
                text="Driver: You are not using an NVIDIA graphics card"
            )

        self.distro_id.configure(text=f"ID: {distro}")


class Nvidia_Top(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#09928B"
        self.title("Nvidia Drive Install")
        self.resizable(0, 0)
        app_width = 900
        app_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.nv_deb = LabelFrame(
            self,
            text="Debian",
            font=("Sans", 12),
            padx=20,
            pady=20,
            background="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
        )
        self.nv_deb.pack(pady=20, padx=20, fill="x", expand=True)

        self.deb_ent_0 = Entry(
            self.nv_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_0.pack(pady=1, padx=5, fill="x")
        self.deb_ent_0.insert(0, f"sudo apt install linux-headers-amd64")

        self.deb_ent_1 = Entry(
            self.nv_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_1.pack(pady=1, padx=5, fill="x")
        self.deb_ent_1.insert(
            0,
            f"deb http://deb.debian.org/debian/ {distribution_info.get('DEBIAN_CODENAME', 'N/A')} main contrib non-free non-free-firmware #Add to:/etc/apt/sources.list",
        )

        self.deb_ent_2 = Entry(
            self.nv_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_2.pack(pady=1, padx=5, fill="x")
        self.deb_ent_2.insert(0, f"sudo apt update")

        self.deb_ent_2 = Entry(
            self.nv_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_2.pack(pady=1, padx=5, fill="x")
        self.deb_ent_2.insert(
            0, f"sudo apt install nvidia-driver firmware-misc-nonfree"
        )

        self.nv_inst_btn = Button(
            self,
            text="Give Me A Terminal",
            borderwidth=0,
            highlightthickness=1,
            command=gimme_term,
        )
        self.nv_inst_btn.pack(pady=20)


class Lutris_Top(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#09928B"
        self.title("Lutris Install")
        self.resizable(0, 0)
        app_width = 400
        app_height = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        def install_lutris_deb():
            # Define the command to run in the terminal

            command = "x-terminal-emulator -e 'bash -c \"flatpak install flathub net.lutris.Lutris -y ; read -p Press_Enter_To_Exit\"'"

            # Run the command in a new terminal
            subprocess.Popen(command, shell=True)

        self.lutris_info = Label(
            self,
            text="This will kick-off a Lutris Terminal Install",
            bg="#09928B",
            fg="#FFFFFF",
        )
        self.lutris_info.pack(pady=20)

        self.lu_inst_btn = Button(
            self,
            text="Do it!",
            borderwidth=0,
            highlightthickness=0,
            command=install_lutris_deb,
        )
        self.lu_inst_btn.pack()


class Steam_Top(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#09928B"
        self.title("Steam Install")
        self.resizable(0, 0)
        app_width = 400
        app_height = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        term_stem = """cd
wget https://cdn.cloudflare.steamstatic.com/client/installer/steam.deb
sudo apt install ./steam.deb

steam"""

        def install_steam_deb():
            # Define the command to run in the terminal

            command = f"x-terminal-emulator -e 'bash -c \"{term_stem} ; read -p Press_Enter_To_Exit\"'"

            # Run the command in a new terminal
            subprocess.Popen(command, shell=True)

        self.steam_info = Label(
            self,
            text="This will kick-off a Steam Terminal Install",
            bg="#09928B",
            fg="#FFFFFF",
        )
        self.steam_info.pack(pady=20)

        self.st_inst_btn = Button(
            self,
            text="Do it!",
            borderwidth=0,
            highlightthickness=0,
            command=install_steam_deb,
        )
        self.st_inst_btn.pack()


class Heroic_Top(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#09928B"
        self.title("Heroic Install")
        self.resizable(0, 0)
        app_width = 400
        app_height = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        def install_heroic_deb():
            # Define the command to run in the terminal
            command = "x-terminal-emulator -e 'bash -c \"flatpak install flathub com.heroicgameslauncher.hgl -y ; read -p Press_Enter_To_Exit\"'"

            # Run the command in a new terminal
            subprocess.Popen(command, shell=True)

        self.heroic_info = Label(
            self,
            text="This will kick-off a Heroic Terminal Install",
            bg="#09928B",
            fg="#FFFFFF",
        )
        self.heroic_info.pack(pady=20)

        self.lu_inst_btn = Button(
            self,
            text="Do it!",
            borderwidth=0,
            highlightthickness=0,
            command=install_heroic_deb,
        )
        self.lu_inst_btn.pack()


class Wine_Top(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#09928B"
        self.title("Wine INstall")
        self.resizable(0, 0)
        app_width = 900
        app_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.wine_deb = LabelFrame(
            self,
            text="Debian",
            font=("Sans", 12),
            padx=20,
            pady=20,
            background="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
        )
        self.wine_deb.pack(pady=20, padx=20, fill="x", expand=True)

        self.deb_ent_0 = Entry(
            self.wine_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_0.pack(pady=1, padx=5, fill="x")
        self.deb_ent_0.insert(1, f"sudo dpkg --add-architecture i386")

        self.deb_ent_1 = Entry(
            self.wine_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_1.pack(pady=1, padx=5, fill="x")
        self.deb_ent_1.insert(0, "sudo mkdir -pm755 /etc/apt/keyrings")

        self.deb_ent_2 = Entry(
            self.wine_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_2.pack(pady=1, padx=5, fill="x")
        self.deb_ent_2.insert(
            0,
            "sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key",
        )

        self.deb_ent_3 = Entry(
            self.wine_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_3.pack(pady=1, padx=5, fill="x")
        self.deb_ent_3.insert(
            0,
            f"sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/{distribution_info.get('DEBIAN_CODENAME', 'N/A')}/winehq-{distribution_info.get('DEBIAN_CODENAME', 'N/A')}.sources",
        )

        self.deb_ent_3 = Entry(
            self.wine_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_3.pack(pady=1, padx=5, fill="x")
        self.deb_ent_3.insert(0, f"sudo apt update")

        self.deb_ent_4 = Entry(
            self.wine_deb, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.deb_ent_4.pack(pady=1, padx=5, fill="x")
        self.deb_ent_4.insert(0, f"sudo apt install --install-recommends winehq-stable")

        self.wine_ub = LabelFrame(
            self,
            text="Ubuntu Base",
            font=("Sans", 12),
            padx=20,
            pady=20,
            background="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
        )
        self.wine_ub.pack(pady=20, padx=20, fill="x", expand=True)

        self.ubuntu_ent_0 = Entry(
            self.wine_ub, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.ubuntu_ent_0.pack(pady=1, padx=5, fill="x")
        self.ubuntu_ent_0.insert(0, f"sudo dpkg --add-architecture i386")

        self.ubuntu_ent_1 = Entry(
            self.wine_ub, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.ubuntu_ent_1.pack(pady=1, padx=5, fill="x")
        self.ubuntu_ent_1.insert(0, "sudo mkdir -pm755 /etc/apt/keyrings")

        self.ubuntu_ent_2 = Entry(
            self.wine_ub, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.ubuntu_ent_2.pack(pady=1, padx=5, fill="x")
        self.ubuntu_ent_2.insert(
            0,
            "sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key",
        )

        self.ubuntu_ent_3 = Entry(
            self.wine_ub, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.ubuntu_ent_3.pack(pady=1, padx=5, fill="x")
        self.ubuntu_ent_3.insert(
            0,
            f"sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/{distribution_info.get('VERSION_CODENAME', 'N/A')}/winehq-{distribution_info.get('VERSION_CODENAME', 'N/A')}.sources",
        )

        self.ubuntu_ent_3 = Entry(
            self.wine_ub, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.ubuntu_ent_3.pack(pady=1, padx=5, fill="x")
        self.ubuntu_ent_3.insert(0, f"sudo apt update")

        self.ubuntu_ent_4 = Entry(
            self.wine_ub, background="#FFFFFF", borderwidth=0, highlightthickness=1
        )
        self.ubuntu_ent_4.pack(pady=1, padx=5, fill="x")
        self.ubuntu_ent_4.insert(
            0, f"sudo apt install --install-recommends winehq-stable"
        )

        if check_debian_release() == True:
            self.wine_ub.pack_forget()

        if check_ubuntu_release() == True:
            self.wine_deb.pack_forget()

        self.wine_inst_btn = Button(
            self,
            text="Give Me A Terminal",
            borderwidth=0,
            highlightthickness=0,
            command=gimme_term,
        )
        self.wine_inst_btn.pack(pady=20)


# [End Of The Line]
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
