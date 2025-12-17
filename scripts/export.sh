#!/usr/bin/env bash
set -euo pipefail

rm -rf export
mkdir export

echo "Exporting dashboards"
docker exec superset_app superset export-dashboards --include-related-assets -f /tmp/dashboards.zip

echo "Exporting roles"
docker exec superset_app superset fab export-roles -path /tmp/roles.json

echo "Export complete"

echo "Coping to host fs"

docker cp superset_app:/tmp/dashboards.zip export/dashboards.zip
docker cp superset_app:/tmp/roles.json export/roles.json
