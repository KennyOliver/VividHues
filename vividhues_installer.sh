#!/bin/bash


NORMAL=$(tput sgr0)

BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
ORANGE=$(tput setaf 3)
BLUE=$(tput setaf 4)
PURPLE=$(tput setaf 5)
CYAN=$(tput setaf 6)

# 3 bits => only 7 possible colors!

printf "
██╗░░░██╗██╗██╗░░░██╗██╗██████╗░██╗░░██╗██╗░░░██╗███████╗░██████╗
██║░░░██║██║██║░░░██║██║██╔══██╗██║░░██║██║░░░██║██╔════╝██╔════╝
╚██╗░██╔╝██║╚██╗░██╔╝██║██║░░██║███████║██║░░░██║█████╗░░╚█████╗░
░╚████╔╝░██║░╚████╔╝░██║██║░░██║██╔══██║██║░░░██║██╔══╝░░░╚═══██╗
░░╚██╔╝░░██║░░╚██╔╝░░██║██████╔╝██║░░██║╚██████╔╝███████╗██████╔╝
░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═════╝░
█▄▀ █▀▀ █▄ █ █▄ █ █▄█ █▀█ █   █ █ █ █▀▀ █▀█
█ █ ██▄ █ ▀█ █ ▀█  █  █▄█ █▄▄ █ ▀▄▀ ██▄ █▀▄
\n"

printf '%.0s-' {1..65}
printf "\n\n"

printf "VividHues & Installer  —  Kenneth Oliver ©2022\n\n"
sleep .5

printf "Hi there! 👋\r"
sleep 1.4

pip show VividHues 1>/dev/null
if [ $? == 0 ]; then
    # python -c "import VividHues; print(VividHues.__version__)"
    printf "VividHues is already installed!\n"
    printf "${CYAN}Would you like to update VividHues?\n"
    updatingPackage="True"
else
    printf "VividHues isn't installed yet!\n"
    printf "${CYAN}Would you like to install VividHues?\n"
    updatingPackage="False"
fi
read -p "    (y/n)  -->    ${NORMAL}" choice

# choice=${choice,,}  # all lowercase
printf "${CYAN}👉 You chose "
case "$choice" in 
  y|Y ) printf "yes";;
  n|N ) printf "no";;
  * ) printf "an invalid choice";;
esac
printf "!${NORMAL}\n\n"
sleep .5

if [[ $choice == y* ]]; then
    if [ $updatingPackage == "True" ]; then
        printf "Looks like we're updating VividHues!!! 👍\n\n"
        printf "$BLUE"
        pip install --upgrade VividHues --disable-pip-version-check
        printf "$NORMAL"
    else
        printf "Looks like we're installing VividHues!!! 👍\n\n"
        printf "$BLUE"
        pip install VividHues --disable-pip-version-check
        printf "$NORMAL"
    fi
    printf "\n"
    printf "${ORANGE}Success! Have colorful fun! 🌈 📦${NORMAL}\n"
    printf "\n"
    sleep 2
fi

printf "Press  enter  to exit!\n"
read pressEnterToExit  # unused variable, but exists for enter to exit
printf "Bye! 👋\n"
sleep 1.5
