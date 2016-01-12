sqlite3 test.db <<EOF
.tables
select * from user;
select * from questionnaire;
EOF
