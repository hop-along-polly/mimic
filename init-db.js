// Creates the IDcore API application user
admin = db.getSiblingDB('admin');
admin.createUser({
	user: 'always-on',    // Should match the DB_USERNAME env var in .env
	pwd: 'always-on-pw',  // Should match the DB_PASSWORD env var in .env
	roles: [{ role: 'readWrite', db: 'always-on' }],
});

// TODO Remove this test data
alwaysOn = db.getSiblingDB('always-on')
alwaysOn.createCollection('manifests')
alwaysOn.getCollection('manifests').insertMany([
  {
    "request": "jwt_req",
    "responses": "jwt_res"
  }
])
