from alwayson.config import Config
from alwayson.db.manifest_repo import ManifestRepo

def inject_manifest_repo():
  cfg = Config.create()
  # TODO In middleware we would need to figure out how to get the
  # org name from the JWT and then pass it here so it selects the
  # correct customer DB
  return ManifestRepo.create(cfg)
