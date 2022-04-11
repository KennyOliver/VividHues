#!/bin/bash

# Kenneth Oliver (c)2022


alert_noise() {
    printf "\a"
}


NORMAL=$(tput sgr0)

# 3 bits => only 7 possible colors!
BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
ORANGE=$(tput setaf 3)  # appears yellow (at least on Windows)
BLUE=$(tput setaf 4)
PURPLE=$(tput setaf 5)
CYAN=$(tput setaf 6)


alert_noise


printf "${CYAN}\
${RED}██╗░░░██╗${ORANGE}██╗${GREEN}██╗░░░██╗${CYAN}██╗${BLUE}██████╗░${PURPLE}██╗░░██╗${RED}██╗░░░██╗${ORANGE}███████╗${GREEN}░██████╗
${RED}██║░░░██║${ORANGE}██║${GREEN}██║░░░██║${CYAN}██║${BLUE}██╔══██╗${PURPLE}██║░░██║${RED}██║░░░██║${ORANGE}██╔════╝${GREEN}██╔════╝
${RED}╚██╗░██╔╝${ORANGE}██║${GREEN}╚██╗░██╔╝${CYAN}██║${BLUE}██║░░██║${PURPLE}███████║${RED}██║░░░██║${ORANGE}█████╗░░${GREEN}╚█████╗░
${RED}░╚████╔╝░${ORANGE}██║${GREEN}░╚████╔╝░${CYAN}██║${BLUE}██║░░██║${PURPLE}██╔══██║${RED}██║░░░██║${ORANGE}██╔══╝░░${GREEN}░╚═══██╗
${RED}░░╚██╔╝░░${ORANGE}██║${GREEN}░░╚██╔╝░░${CYAN}██║${BLUE}██████╔╝${PURPLE}██║░░██║${RED}╚██████╔╝${ORANGE}███████╗${GREEN}██████╔╝
${RED}░░░╚═╝░░░${ORANGE}╚═╝${GREEN}░░░╚═╝░░░${CYAN}╚═╝${BLUE}╚═════╝░${PURPLE}╚═╝░░╚═╝${RED}░╚═════╝░${ORANGE}╚══════╝${GREEN}╚═════╝░${NORMAL}
█▄▀ █▀▀ █▄ █ █▄ █ █▄█  █▀█ █   █ █ █ █▀▀ █▀█
█ █ ██▄ █ ▀█ █ ▀█  █   █▄█ █▄▄ █ ▀▄▀ ██▄ █▀▄
\n"

printf '%.0s—' {1..65}
printf "\n\n"

printf "${PURPLE}VividHues Instant Installer  —  Kenneth Oliver ©2022${NORMAL}\n\n"
sleep .5

printf "Hi there! 👋\r"
sleep 1


# (the below) cannot be part of if statement,
#     otherwise it thinks VividHues is never installed
pip show VividHues 1>/dev/null
if [ $? == 0 ]; then
    # python -c "import VividHues; print(VividHues.__version__)"
    printf "VividHues is already installed! :P\n"
    printf "${CYAN}Would you like to update VividHues?\n"
    updatingPackage="True"
else
    printf "VividHues isn't installed yet! :o\n"
    printf "${CYAN}Would you like to install VividHues?\n"
    updatingPackage="False"
fi
printf "    (y/n)  -->    ${NORMAL}"
read -r choice
choice=${choice,,}  # all lowercase


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
        printf "Looks like we're updating VividHues!!! 👍\n"
        printf "$BLUE"
        pip install --upgrade VividHues --disable-pip-version-check &>/dev/null
        # &>/dev/null  is used to redirect stdout to null
        #              so that output is "hidden"
        printf "$NORMAL"
    else
        printf "Looks like we're installing VividHues!!! 👍\n\n"
        printf "$BLUE"
        pip install VividHues --disable-pip-version-check
        printf "$NORMAL"
    fi
    printf "\n"
    printf '%.0s—' {1..65}
    printf "\n\n"
    printf "${ORANGE}Success! Have colorful fun! 🌈 📦${NORMAL}\n"
    printf "\n"
    alert_noise
    sleep 2
fi


printf "Press  enter  to exit!\n"
read -r pressEnterToExit  # unused variable, but exists for enter to exit
printf "Bye! 👋\n"
alert_noise
sleep 1.5
