#!/bin/bash
clear
echo "#########################################"
echo "#--#####--#8888888888888888888#--#####--#"
echo "##--###--##88 1. Termux     88##--###--##"
echo "###--#--###88 2. Other      88###--#--###"
echo "####---####88 3. iSH (IOS)  88####---####"
echo "###--#--###8888888888888888888###--#--###"
echo "##--###--##88 Choose 1/2/3: 88##--###--##"
echo "#--#####--#8888888888888888888#--#####--#"
echo "#########################################"
read numb
if [ $numb = "1" ]
then
	pkg install python
	pkg install dos2unix
	pip install requests colorama proxyscrape
	cp ~/Bomber/spammer.py $PREFIX/binBomber
	dos2unix $PREFIX/bin/Bomber
	chmod -R 777 ~/Bomber
	chmod 777 $PREFIX/bin/Bomber
	Bomber
else
	if [ $numb = "2" ]
	then
		if [ "$(whoami)" != 'root' ];
		then
			echo "You have no rights. Run install.sh with root (sudo sh ~/Bomber/install.sh)"
			exit
		else
			apt install python3 python3-pip dos2unix
			pip3 install requests colorama proxyscrape
			cp ~/Bomber/spammer.py $PREFIX/bin/Bomber
			dos2unix $PREFIX/bin/Bomber
			chmod 777 $PREFIX/bin/Bomber
			chmod -R 777 ~/Bomber
			Bomber
		fi
	else
		if [ $numb = "3" ] 
		then
			apk add python
			apk add python3
			apk add dos2unix
			pip3 install requests
			pip3 install colorama
			pip3 install proxyscrape
			cp ~/Bomber/spammer.py /usr/bin/Bomber
			dos2unix /usr/bin/Bomber
			chmod 777 /usr/bin/Bomber
			Bomber
		else
			echo "Invalid input"
		fi
	fi
fi
