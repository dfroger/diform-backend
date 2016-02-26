if [ "$#" != 1 ]
then
    echo "Usage: print_db.sh FILE.DB"
fi

TABLE_NAME=$1

sqlite3 $TABLE_NAME <<EOF
.tables
select * from user;
select * from questionnaire;
EOF
