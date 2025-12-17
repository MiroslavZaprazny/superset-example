#!/usr/bin/env bash
set -euo pipefail

echo "Importing roles"
docker exec superset_app superset fab import-roles --path assets/roles.json

echo "Creating dashboards ZIP"
cd assets
rm -f dashboards.zip
zip -r dashboards.zip dashboards charts datasets databases metadata.yaml

echo "Ensuring admin user exists"
docker exec superset_app superset fab create-admin \
  --username admin \
  --firstname Admin \
  --lastname User \
  --email admin@example.com \
  --password admin || true
#
echo "Importing dashboards"
docker exec superset_app superset import-dashboards -u admin -p assets/dashboards.zip
rm -f dashboards.zip
#
# echo "Import complete"
