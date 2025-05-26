admin = db.getSiblingDB('admin');
admin.createUser({
	user: 'mimic',  // Should match the DB_USERNAME env var in .env
	pwd: 'mimic-pw',  // Should match the DB_PASSWORD env var in .env
	roles: [{ role: 'readWrite', db: 'mimic' }],
});
