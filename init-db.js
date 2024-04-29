// Creates the IDcore API application user
db = db.getSiblingDB('admin');
db.createUser({
	user: 'always-on',
	pwd: 'always-on-pw',
	roles: [{ role: 'readWrite', db: 'always-on' }],
});
