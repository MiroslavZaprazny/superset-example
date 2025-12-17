# taken from official docs https://superset.apache.org/docs/6.0.0/installation/docker-builds/

FROM apache/superset:5.0.0

USER root

# Install packages using uv into the virtual environment
# Superset started using uv after the 4.1 branch; if you are building from apache/superset:4.1.x or an older version,
# replace the first two lines with RUN pip install \
RUN . /app/.venv/bin/activate && \
    uv pip install \
    # install psycopg2 for using PostgreSQL metadata store - could be a MySQL package if using that backend:
    psycopg2-binary \
    # package needed for using single-sign on authentication:
    Authlib \
    # Pillow for Alerts & Reports to generate PDFs of dashboards
    Pillow

# Switch back to the superset user
USER superset

CMD ["/app/docker/entrypoints/run-server.sh"]
