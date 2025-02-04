admin = db.getSiblingDB('admin');
admin.createUser({
	user: 'testerozza',  // Should match the DB_USERNAME env var in .env
	pwd: 'testerozza-pw',  // Should match the DB_PASSWORD env var in .env
	roles: [{ role: 'readWrite', db: 'testerozza' }],
});
