// Creates the IDcore API application user
admin = db.getSiblingDB('admin');
admin.createUser({
	user: 'always-on',    // Should match the DB_USERNAME env var in .env
	pwd: 'always-on-pw',  // Should match the DB_PASSWORD env var in .env
	roles: [{ role: 'readWrite', db: 'always-on' }],
});
