USERNAME=$1
PASSWORD=$2

APPCODE=$3

# for row in `ls marklists`
# do
python ./downloadLatestReports.py $USERNAME $PASSWORD $APPCODE
python ./createMarkList.py -A $APPCODE  -U $USERNAME -P $PASSWORD
python ./createApplicationList.py -A $APPCODE  -U $USERNAME -P $PASSWORD
python ./markNotApplicableComponents.py -A $APPCODE  -U $USERNAME -P $PASSWORD
# done
