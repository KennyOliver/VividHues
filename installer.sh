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


printf "Hi there!\n"
sleep .5
printf "${CYAN}Would you like to install VividHues?\n"
read -p "    (y/n)  -->    ${NORMAL}" choice
# choice=${choice,,}  # all lowercase
printf "$CYAN 👉 You chose "
case "$choice" in 
  y|Y ) printf "yes";;
  n|N ) printf "no";;
  * ) printf "an invalid choice!";;
esac
printf "$NORMAL\n"
sleep .5

if [[ $choice == y* ]]; then
    printf "Looks like we're installing VividHues!!! 👍\n"
    printf "$BLUE"
    pip install VividHues
    printf "$NORMAL"
    printf "$ORANGE Success! Have colorful fun! 🌈 📦$NORMAL\n"
    sleep 5
fi

printf "Bye! 👋\n"
sleep 1.5
