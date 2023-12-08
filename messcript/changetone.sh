file="$1"
replaceString="wav"
secondSearchString="mp4"
thirdSearchString="mp3"
echo $replaceString
echo $secondSearchString
echo $thirdSearchString
mystr1=$file


if [[ $mystr1 == *"$secondSearchString"* ]]
then

mystr2="${mystr1/$secondSearchString/$replaceString}"
echo " ok $mystr2"
else
mystr2=$mystr1
fi
echo $mystr2
echo "mystr2"




if [[ $mystr2 == *"$thirdSearchString"* ]]
then
echo " ok ${mystr2/$thirdSearchString/$replaceString}"
mystr3="${mystr2/$thirdSearchString/$replaceString}"
else
mystr3=$mystr2
fi
echo $mystr3
echo "ok str"

if [ -z "$mystr3" ]; then
	echo "arg is empty #1"
fi

if [ -v "$mystr3" ]; then
	echo "arg is empty#2"
fi
if [ -n "$mystr3" ]; then
  echo "not empty #3"
  ffmpeg -i $1 $mystr3

fi

